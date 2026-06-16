import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    """
    Determines if a given year is a leap year.
    Returns True if leap year, False otherwise.
    """
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    """
    Returns the number of days in a specific month.
    Takes into account whether it's a leap year for February.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


# Get user input
name = input("input your name: ")
age = input("input your age: ")

# Get current local time
localtime = time.localtime(time.time())

# Convert age string to integer
year = int(age)

# Calculate total months (age in years * 12 + current month)
month = year * 12 + localtime.tm_mon

# Initialize day counter
day = 0

# Calculate birth year and end year
begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days from birth year to current year
# Loop through each year and add 366 for leap years, 365 for non-leap years
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

# Check if current year is a leap year
leap_year = judge_leap_year(localtime.tm_year)

# Add days for each month that has passed in the current year
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

# Add days from the current month that have passed
day = day + localtime.tm_mday

# Display results
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
