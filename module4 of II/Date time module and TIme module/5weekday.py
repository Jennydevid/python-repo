import datetime

d = datetime.date(2022, 11, 12)
print(d.month)

# method to know the day of the week where 0-mon and 6-sun
day = d.weekday()
print(day)

#method to get the week day where 1-mon and 7-sun
day1 =d.isoweekday()
print(day1)

