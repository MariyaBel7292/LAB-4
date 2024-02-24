#1
from datetime import date, timedelta 

day = date.today() - timedelta(5)
print("Current date is ", date.today())
print("Before 5 days ", day)

#2
from datetime import date, timedelta
tod = date.today()
yes = date.today() - timedelta(1)
tom = date.today() + timedelta(1)
print("Yesterday :",yes)
print("Today :", tod )
print("Tomorrow :", tom)


#3
import datetime
a = datetime.datetime.now()
b = datetime.datetime.now().replace(microsecond=0)
print(a)
print(b)


#4
from datetime import datetime
a = datetime.today()
b = datetime.strptime("14 February 2024, 07:00:00", "%d %B %Y, %H:%M:%S")
delta = a - b
c = delta.total_seconds()
print(a)
print(c)