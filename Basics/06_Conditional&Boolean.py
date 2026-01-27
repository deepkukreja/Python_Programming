if(True):
   print('Conditional was True')
if(False):                            # Nothing will come as output
   print('Conditional was False')


Language = 'Python'
if Language == 'Python':
    print('Conditional was True')


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is
 

Language = 'Python'
if Language == 'Python':
    print('Language is Python')
else:
    print('No Match')



Language = 'Java'
if Language == 'Python':
    print('Language is Python')
else:
    print('No Match')



Language = 'Java'
if Language == 'Python':
    print('Language is Python')
elif Language == 'Java':
    print('Language is Java')
elif Language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
#Note - Python doesn't have switch statement cuz if elif and else is sufficient to do all the work







#and
#or
#not

user = 'Admin'
Logged_In =True
if user == 'Admin' and Logged_In:
    print('Admin Page')
else:
    print('Bad Credentials')





user = 'Admin'
Logged_In =False
if user == 'Admin' and Logged_In:
    print('Admin Page')
else:
    print('Bad Credentials')



user = 'Admin'
Logged_In =True
if user == 'Admin' or Logged_In:
    print('Admin Page')
else:
    print('Bad Credentials')


user = 'Admin'
Logged_In =False
if not Logged_In:
    print('Log In Please')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b) # False Outcome
print(id(a))
print(id(b))


a = [1, 2, 3]
b = a
print(a is b)
print(a == b)
print(id(a) == id(b))



# False Values:
# False
# None
# Zero of any numeric type.
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

Condition = False
if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



Condition = None
if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')




Condition = 0
if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



Condition = 10
if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


Condition = {}
if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')