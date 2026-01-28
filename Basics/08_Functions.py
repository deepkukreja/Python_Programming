def hello_fcn():   
     pass   #If we don't have to add anything now but want to add in future and doesn't want it to give error

print(hello_fcn()) #It will give none



def hello_fcn():
     print('Hello World')

hello_fcn()
hello_fcn()
# DRY - Don’t Repeat Yourself



def hello_fcn():
     return ('Hello World')  #return statement sends a value back from a function and terminates its execution.

print(hello_fcn())
print(hello_fcn().upper())



def hello_fcn(greeting, name='You'):
     return'{}, {}'.format(greeting, name)

print(hello_fcn('Hi', name='Deep'))


def student_info(*args, **kwargs):
     print(args)    #args is just a name (you can call it anything), * is the important part. It collects extra arguments into a tuple
     print(kwargs)  #kwargs = keyword arguments, ** collects them into a dictionary

student_info('Art', 'Math', name= 'John',age = 22)



def student_info(*args, **kwargs):
     print(args)
     print(kwargs) 

courses = ['Math', 'Art']
info = { 'name' : 'John', 'age': 22}

student_info(courses, info) # PROBLEM: You are passing 'courses' and 'info' as normal arguments. So Python treats BOTH of them as positional arguments (*args).That’s why: args = (['Math', 'Art'], {'name': 'John', 'age': 22}) and kwargs = {}
student_info(*courses, **info)




# Number of days per month.
# First value is a placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    """Return True for leap years, False for non-leap years.""" #Docstring
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

# Example usage
print(is_leap(2024))           # True
print(days_in_month(2024, 2)) # 29
print(days_in_month(2023, 2)) # 28
print(days_in_month(2023, 13))# Invalid Month


