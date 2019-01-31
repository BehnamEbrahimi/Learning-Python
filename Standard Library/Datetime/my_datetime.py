import datetime

# Naive: they dont know daylight saving and time zones
d = datetime.date(2001, 9, 11)  # year, month, day. important: dont pass 09
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
# weekday() - Monday is 0 and Sunday is 6
print(tday.weekday())
# isoweekday() - Monday is 1 and Sunday is 7
print(tday.isoweekday())

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(days=12)
print(tday - tdelta)  # the date  in 12 days ago

bday = datetime.date(1985, 1, 28)
till_bday = tday - bday  # by adding or subtracting two days, we will have a timedelta
print(till_bday)
print(till_bday.days)  # just return the days
print(till_bday.seconds)  # just returns the seconds. it does not convert days to seconds
print(till_bday.total_seconds())  # convert timedelta to seconds

# datetime.time is rarely used. instead use datetime.datetime
t = datetime.time(9, 30, 45, 100000)  # hr, min, sec, microsecond
print(t)
print(t.hour)

# datetime.datetime
dt_today = datetime.datetime.today()  # year, month, day, hour, min, sec, milisec
print(dt_today.time())  # just returns the time
print(dt_today.date())  # just returns the date
print(dt_today.year)
tdelta = datetime.timedelta(days=1, hours=5)
print(dt_today + tdelta)  # 1 day and 5 hours to the future

dtnow = datetime.datetime.now()  # the difference between this and today() is that today() gives the local time and now() takes a parameter for timezone and if it's left off, it is exactly the same as today()
# print(dir(datetime.datetime))
dt_utcnow = datetime.datetime.utcnow()  # returnd the utc. important: it is not timezone aware also
print(dt_today)
print(dtnow)
print(dt_utcnow)

import pytz  # third party package needs to be installed: pip install pytz
# even in the Python document, they recommend using pytx
# dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))

dt = datetime.datetime(2019, 1, 31, 16, 20, 10, tzinfo=pytz.UTC)  # we passed a datetime and secified the time zone to utc which is why we will have +00:00 at the end
print(dt)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)  # returns the current moment at the UTC which is time zone-aware
print(dt_utcnow)

dt_syd = dt_utcnow.astimezone(pytz.timezone('Australia/NSW'))  # how to convert dt_utcnow to Sydney time +11:00
print(dt_syd)

# for tz in pytz.all_timezones:  # this is how we get all time zones
#     print(tz)

dt_syd = datetime.datetime.now()  # not time zone-aware. if we apply astimezone() method on this, we will face error. because it is naive
print(dt_syd)


syd_tz = pytz.timezone('Australia/NSW')
dt_syd = syd_tz.localize(dt_syd)  # this is how we convert naive datatime to a time zone aware one
print(dt_syd)

dt_perth = dt_syd.astimezone(pytz.timezone('Australia/Perth'))
print(dt_perth)

# strftime - Datetime to String
# strptime - String to Datetime
print(dt_syd.isoformat())
print(dt_syd.strftime('%B %d, %Y'))  # format codes from Python documentation

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
