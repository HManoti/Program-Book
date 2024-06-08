#random module- random number generation
import random
print(random.randrange(5))     

print(random.randrange(20,50,2))     #last value not included

print(random.randint(1,10))  #last value included


import math
print(math.sqrt(16))
print(math.pi)
print(math.ceil(4.45))       #upper value
print(math.floor(4.45))      #lower value
print(math.factorial(5))
print(math.fabs(-34))
print(math.pow(2,3))


#Date time module
import datetime
print(datetime.datetime(2023,3,21))   #year,month,date    hour,minute,second


import datetime
x=datetime.datetime.today()
y=datetime.datetime(2003,2,16)
print(x-y)

import calendar
print(calendar.month(2023,3))

import calendar
for i in range(1,13):
    print(calendar.month(2023,i))

import time
import datetime
print(datetime.datetime.now())

print(datetime.date.today().strftime("%B"))    #month of year

print(datetime.date.today().strftime("%W"))    #day of month

print(datetime.date.today().strftime("%w"))    #day of week

print(datetime.date.today().strftime("%j"))    #day of year

print(datetime.date.today().strftime("%d"))    #day of month 

print(datetime.date.today().strftime("%A"))    #day of week
