from datetime import date

d = date(2016, 12, 8)
print(d)

d1 = d.replace(month = 11, day = 7, year = 2015)  # the replace method returns a changed object so it must be assigned to a variable
print(d1)