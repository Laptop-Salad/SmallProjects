"""
Calendar Maker
"""

import datetime

day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Get how many days are in a month, e.x. 28, 31
def get_days_month(month, year):
    try:
        for day in range(1, 32): 
            datetime.datetime(year, month, day)
    except:
        # If in above loop day is 31 and it fails, then we need to minus 1
        day -= 1

    return day  
    
# Get year from user
print("Enter the year for the calendar:")
year = input(">")

while not year.isnumeric() or len(year) != 4:
    print("Please enter a year with the format 1234:")
    year = input(">")

year = int(year)
   
# Get month from user
print("Enter the month for the calendar, 1-12:")
month = input(">")

while not month.isnumeric() or not (int(month) > 0 and int(month) < 13):
    print("Please enter a month 1-12:")
    month = input(">")

month = int(month)

# See how many days in month
days = get_days_month(month, year)

# Get the first day and name of day, of the month
first_day = datetime.datetime(year, month, 1)
day_name = day_names.index(first_day.strftime("%A"))     

day_lines = []

# How many days before start of first day of month

# See how many days before month
if month == 1:
    previous_month = get_days_month(12, year-1)
else:
    previous_month = get_days_month(month-1, year)

days_before = len(day_names) - day_name
previous_month -= (days_before - 1)

for day in range(0, days_before):
    formatted_day = str(previous_month)
    
    if len(formatted_day) == 1:
        formatted_day = "0" + formatted_day
    
    day_lines.append("|{}        ".format(formatted_day))
    previous_month += 1
  
day = 0

# Create line with day number for calendar
for day in range(0, days):
    formatted_day = str(day+1)
    
    if len(formatted_day) == 1:
        formatted_day = "0" + formatted_day
    
    day_lines.append("|{}        ".format(formatted_day))
    
# Print top of calendar
print("+----------" * 7, end="+\n")

# Keep track of how many boxes are printed per line : max 7
count = 0

# Print calendar
for i in range(0, len(day_lines)):
    if count == 7:
        print("|")
        print("|          " * 7, end='|\n')
        print("|          " * 7, end='|\n')
        print("|          " * 7, end='|\n')
        print("+----------" * 7, end='|\n')
        count = 0
    else:
        print(day_lines[i], end='')
        count += 1

days_after = 1
while count < 7:
    print("|{}        ".format("0" + str(days_after)), end='')
    days_after += 1
    count += 1
    
print("|")
print("|          " * 7, end='|\n')
print("|          " * 7, end='|\n')
print("|          " * 7, end='|\n')
print("+----------" * 7, end='|\n')
