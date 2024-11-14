# import
import pandas as pd
import duckdb
import os
import smtplib
from email.mime.text import MIMEText
from pretty_html_table import build_table

# fuel - data
fuel_df = pd.read_csv("https://github.com/shithi30/Gas_Price_QA_CICD_GreatExpectations/blob/main/Today's%20Fuel%20Prices.csv?raw=true")

# fuel - summary
qry = '''
select price, station, address, city, report_time 
from fuel_df 
where city = 'Windsor' and address like '%Tecumseh%' and price < 140
'''
summ_df = duckdb.query(qry).df()

# email - from, to, body
sender_email = "shithi30@gmail.com"
receiver_email = ["shithi30@outlook.com", "Purnabchowdhury@gmail.com"]
body = '''
Please find below, today's gasoline prices (¢/L).
''' + build_table(summ_df, "yellow_dark", font_size = "12px", text_align = "left") + '''
Full list of prices across Windsor-Essex? Click <a href="https://github.com/shithi30/Gas_Price_QA_CICD_GreatExpectations/blob/main/Today's%20Fuel%20Prices.csv">here</a>.<br><br>
Thanks,<br>
Shithi Maitra<br>
Ex Asst. Manager, CS Analytics<br>
Unilever BD Ltd.<br>
'''

# email - object
html_msg = MIMEText(body, "html")
html_msg["Subject"] = "Gas Prices - Refill!"
html_msg["From"] = "Shithi Maitra"
html_msg["To"] = ", ".join(receiver_email)

# email - send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
   server.login(sender_email, os.getenv("EMAIL_PASS"))
   if summ_df.shape[0] > 0: server.sendmail(sender_email, receiver_email, html_msg.as_string())
