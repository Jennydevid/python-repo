from datetime import datetime

obj = datetime.strptime('November 4, 2020 , 14:53:00','%B %d, %Y , %H:%M:%S')

print(obj.strftime('%Y/%m/%d %H:%M:%S'))
print(obj.strftime('%y/%B/%d %H:%M:%S %p'))
print(obj.strftime('%a, %Y %b %d'))
print(obj.strftime('%A, %Y %B %d'))
print("Weekday: ", obj.strftime('%u'))
print("Day of the year: ", obj.strftime("%j"))
print("Week number of the year: ", obj.strftime("%U"))
