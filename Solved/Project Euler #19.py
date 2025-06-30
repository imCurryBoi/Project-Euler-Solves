days_in_a_month = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_days_in_a_month = [31,29,31,30,31,30,31,31,30,31,30,31]
year = 1901
sundays = 0
day_of_the_week = 2  # 1 Jan 1901 was a Tuesday

def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

while year < 2001:
    if is_leap_year(year):
        for days in leap_days_in_a_month:
            if day_of_the_week == 0:  # Sunday
                sundays += 1
            day_of_the_week = (day_of_the_week + days) % 7
    else:
        for days in days_in_a_month:
            if day_of_the_week == 0:  # Sunday
                sundays += 1
            day_of_the_week = (day_of_the_week + days) % 7
    year += 1

print(sundays)
'''
import datetime
sundays = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		if datetime.datetime(year, month, 1).weekday() == 6:
			sundays += 1
print(sundays)
'''