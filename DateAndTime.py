# Print current date and time in Python
from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

# Output Tuesday 25 February 2020