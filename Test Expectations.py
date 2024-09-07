# import
import great_expectations as gx

# fuel data to test
fuel_gx = gx.read_csv("https://github.com/shithi30/Gas_Price_QA_CICD_GreatExpectations/blob/main/Today's%20Fuel%20Prices.csv?raw=true")

# data quality tests
test_results = fuel_gx.validate(expectation_suite = "fuel_data_expectations.json")

# results
if test_results["success"]: print("Data quality tests passed.")
else:
    fail_note = ""
    for result in test_results["results"]:
        if not result["success"]:
            fail_note = fail_note + str(result["expectation_config"]) + "\n"
    raise Exception("Data quality tests failed. Deails below.\n" + fail_note)
