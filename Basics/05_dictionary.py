'''
student = {'name': 'John', 'Age': 25, 'Courses': ['Maths','CompSci'] }
print(student)
print(student['Courses'])
print(student['name'])
# print(student['phone']) #KeyError : Phone is not defined
print(student.get('name'))
print(student.get('phone')) #It will give none
print(student.get('phone', 'Not_Found')) #Now instead of none, we'll get not found
'''

'''
student = {'name': 'John', 'Age': 25, 'Courses': ['Maths','CompSci'] }
student['phone'] = '5555-5555'
student['name'] = 'Joe'
print(student)
'''

'''
#Some problem in this
student = {'name': 'John', 'Age': 25, 'Courses': ['Maths','CompSci'] }
student.update = ({'name': 'Deep', 'Age': 18,'Courses': ['Electronics', 'ComputerScience'], 'Phn. No.': '1111-1111'})
print(student)
'''


'''
student = {'name': 'John', 'Age': 25, 'Courses': ['Maths','CompSci'] }
del student['Age']
print(student)
'''


student = {'name': 'John', 'age': 25, 'Courses': ['Maths','CompSci'] }
age = student.pop('age')
print(student)
print(age)


student = {'name': 'John', 'age': 25, 'Courses': ['Maths','CompSci'] }
print(len(student))  
print(student.keys())
print(student.values())
print(student.keys())
for keys in student:
   print(keys)
for keys, values in student.items():
   print(keys, values)