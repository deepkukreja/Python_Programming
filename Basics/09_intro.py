import mymodule_09
courses = ['History', 'Maths', 'Physics', 'CompSci']
index = mymodule_09.find_index(courses, 'Maths')
print(index)


import mymodule_09 as mm
courses = ['History', 'Maths', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Maths') #it's als okay to consider above as something and write it's full original form below
print(index)

from mymodule_09 import find_index, test # We avoid "import *" because it reduces readability, can cause name conflicts, imports unnecessary items, and makes debugging harder
import sys
courses = ['History', 'Maths', 'Physics', 'CompSci']
index = mymodule_09.find_index(courses, 'Maths')
print(index)
print(test)
print(sys.path)  # sys.path shows the list of directories where Python looks for modules while importing



import random # import random is used to generate random numbers and make random choices in Python
courses = ['History', 'Maths', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)


import math

rads = math.radians(90)
print(rads)   # rads stores the angle value converted into radians
print(math.sin(rads))   # math.sin(rads) calculates the sine of the angle (in radians)




import datetime
import calendar
courses = ['History', 'Math', 'Physics', 'CompSci']
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))



import os
courses = ['History', 'Math', 'Physics', 'CompSci']
print(os.getcwd())  #cwd = current working directory
print(os.__file__) # os.__file__ shows the file path where the os module is located on the system


import antigravity

