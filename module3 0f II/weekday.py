#y mera likha code 
class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #

    def __init__(self, day):
        self.__day = day.title()
        self.__days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __str__(self):
        if self.__day in self.__days:
            return self.__day
        else:
            raise WeekDayError
        
    def add_days(self, n):
        count = self.__days.index(self.__day) + n
        while count > 6:
            count -= 7
        self.__day = self.__days[count]
            
    def subtract_days(self, n):
        count = self.__days.index(self.__day) - n
        while count < 0:
            count += 7
        self.__day = self.__days[count]
   
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
    print(weekday)

except WeekDayError:
    print("Sorry, I can't serve your request.")


#module wala version
class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
