from datetime import timedelta

obj = timedelta(weeks = 3, hours = 5, milliseconds = 67)
print(obj)
print(obj.days)
print(obj.seconds)
print(obj.microseconds)
print(type(obj))