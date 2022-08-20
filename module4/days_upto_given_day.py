def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
           

           #returns the days in the given month
def days_in_month(year, month):
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return 29
    elif year <= 0 or month <= 0 :
        return 0
    return month_day[month-1]


             #returns the number of days of the given year
def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    days += day
    return days


            #testing the code
print(day_of_year(2000, 12, 31))
year = [2000, 2008, 2100, 2017, 2022]
month = [12, 5, 11, 12, 12]
day = [31, 31, 30, 30, 31]
result = [366, 152, 334, 364, 365]
for i in range(len(year)):
    print(year[i], month[i], day[i] ," -> ",end="")
    days = day_of_year(year[i], month[i], day[i])
    print(days)
    if result[i] == days:
        print("ok")
    else:
        print("failed")
