import calendar

#creating calendar object
obj = calendar.Calendar(calendar.FRIDAY)
    #iterweekdays gives an iterator of the weekdays
for i in obj.iterweekdays():
    print(i, end = " ")