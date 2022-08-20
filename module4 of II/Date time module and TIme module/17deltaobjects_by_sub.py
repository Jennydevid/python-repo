#delta objects can be created by subtracting two date or datetime objects

from datetime import datetime, date

do1 = date(2020, 12, 11)
do2 = date.today()

print(do2 - do1) #this is the timedelta object from date object

dt1 = datetime(2020, 12, 11, 12, 10, 33)
dt2 = datetime.today()

print(dt2 - dt1)   # timedelta object from datetime object


