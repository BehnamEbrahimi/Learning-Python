import calendar

print(calendar.isleap(2019))
print(calendar.isleap(2020))
print(calendar.monthrange(2018, 1)) # returns a tuple. 0 is the weekday of the start of the month and 1 is the total number of days in that month
