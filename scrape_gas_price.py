
from datetime import datetime, timedelta

with open("Gas Price Data.txt", "w") as file:
    file.write("This is written at " + str(datetime.now()-timedelta(hours=4)))
