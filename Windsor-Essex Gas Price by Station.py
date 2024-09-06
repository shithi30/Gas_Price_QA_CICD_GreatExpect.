# import
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# open window
Display(visible = 0, size = (1920, 1080)).start()
driver = webdriver.Chrome()
driver.get("https://windsorite.ca/gas/")

# soup
soup = BeautifulSoup(driver.page_source, "html.parser")
tables = soup.find_all("table", attrs = {"id": "prices"})[1:]

# scrape
fuel_df = pd.DataFrame(columns = ["price", "station", "address", "city", "report_time"])
for table in tables: 
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all(["td", "th"])
        cell_values = [cell.get_text(strip = True) for cell in cells]
        if cell_values[0] in ["Price", ""]: continue
        cell_values[1] = cell_values[1].split(cell_values[2])[0]
        fuel_df = pd.concat([fuel_df, pd.DataFrame([cell_values], columns = fuel_df.columns)], ignore_index = True)

# save
fuel_df.to_csv("Today's Fuel Prices.csv", index = False)

# close window
driver.close()
