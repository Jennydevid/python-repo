#date and time can be represented as separate objects or as one. 
from datetime import datetime

dt = datetime(2022, 8, 5, 13, 21, 20)
print('Datetime: ',dt)
print('Time: ',dt.time())
print('Date: ',dt.date())