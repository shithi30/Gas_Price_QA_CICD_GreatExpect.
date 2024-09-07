# import
import pandas as pd
import great_expectations as gx
from datetime import datetime, timedelta

# fuel data
fuel_df = pd.read_csv("https://github.com/shithi30/Gas_Price_QA_CICD_GreatExpectations/blob/main/Today's%20Fuel%20Prices.csv?raw=true")
fuel_df.head()

# context
fuel_df_gx = gx.from_pandas(fuel_df)

# expectations
test1 = fuel_df_gx.expect_column_values_to_be_between("price", 120.00, 200.00)
test2 = fuel_df_gx.expect_column_values_to_be_unique("address")
test3 = fuel_df_gx.expect_column_most_common_value_to_be_in_set("station", ["Petro-Canada", "Esso"], ties_okay = True)
test4 = fuel_df_gx.expect_column_values_to_be_in_set("city", ["Windsor", "Leamington", "Tecumseh", "Kingsville", "LaSalle", "Tilbury", "Essex", "Maidstone", "Amherstburg", "Belle River"])
test5 = fuel_df_gx.expect_column_values_to_be_between("report_time_formatted", min_value = datetime.now() - timedelta(hours = 36), max_value = None) 

# suite
fuel_df_gx.save_expectation_suite("fuel_data_expectations.json")
