This repository holds competitive fuel price analytics, for the most cost-efficient refueling of our family vehicle. <br>

Tech stack: ```Selenium + bs4``` ```Great Expectations``` ```duckdb```  ```GitHub Actions```<br>

### Data Validation - Great Expectations
```Python
test1 = fuel_df_gx.expect_column_values_to_be_between("price", 120.00, 200.00)
test2 = fuel_df_gx.expect_column_values_to_be_unique("address")
test3 = fuel_df_gx.expect_column_most_common_value_to_be_in_set("station", ["Petro-Canada", "Esso"], ties_okay = True)
test4 = fuel_df_gx.expect_column_values_to_be_in_set("city", ["Windsor", "Leamington", "Tecumseh", "Kingsville", "LaSalle", "Tilbury", "Essex", "Maidstone", "Amherstburg", "Belle River"])
test5 = fuel_df_gx.expect_column_values_to_be_between("report_time_formatted", min_value = datetime.now() - timedelta(hours = 36), max_value = None) 
 ```

### Notifiers - Auto. Emails
<p align="center">
  <img width="400" alt="c5" src="https://github.com/user-attachments/assets/450eccf3-adf8-4dc2-8251-8435a6344e0b"><br>
</p>

### Prices Today - Full [List](https://github.com/shithi30/Gas_Price_QA_CICD_GreatExpectations/blob/main/Today's%20Fuel%20Prices.csv)
<p align="center">
  <img width="600" alt="c5" src="https://github.com/user-attachments/assets/65aa22b2-13d1-45ab-8efc-db077884b062"><br>
</p>

<p align="center">
  <strong>Note</strong>: Scraper complies with robots.txt regulations.
</p>


