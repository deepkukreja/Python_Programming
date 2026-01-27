'''
Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
print(Days)
print(len(Days))
print(Days[0][3]) #Here d letter of 0 ie sunday will get printed
print(Days[-1]) #Here values from last will get printed
print(Days[:2]) #It means print values starting from first place upto second where 3rd is not included
print(Days[2:]) #Starting from 2 all the way till it reaches the end
'''

"""
Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
Days.append('Thursday') #Adds Thursday to last
Days.insert(0, 'Saturday') #To add something at a specific location
print(Days)
"""

'''
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2) #This will print who;le seconfd list in 1 with brackets
print(courses)
'''

"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2) #It will add intividual items in the last while if we use append then it it will add all the list(with square brackets)
print(courses)
"""

'''
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
courses.remove('Mathematics') #To remove the element that we don't need any more
print(courses)
'''

'''
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
popped = courses.pop()  #It will automatically remove the last element
print(courses)
print(popped)
'''


"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
courses.reverse() #It will just reverse our list
print(courses)
"""


"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
nums = [3, 7, 11, 1, 99, 41, 22]
courses.sort() #TO sort courses based on alphabetical order
nums.sort() #To sort numbers based on increasing order
print(courses)
print(nums)
"""


'''
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
nums = [3, 7, 11, 1, 99, 41, 22]
courses.sort(reverse=True) #It will sort all the courses based on descending alphabatical order
nums.sort(reverse=True) #It will sort all the numbers based on descending order
print(courses)
print(nums)
'''

"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
nums = [3, 7, 11, 1, 99, 41, 22]
sorted_courses = sorted(courses)  #To sort the courses without altering the original list
print(sorted_courses)
print(max(nums))
print(min(nums))
print(sum(nums)) 
print(courses.index('CompSci')) #To find position of a string in list
print('Art' in courses) #To find whether given element is there in the list
print('Mathematics' in courses)
"""

"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
for item in courses: #Here we can use any word at place of item
    print(item)
for index, course in enumerate(courses): #To get index along with value
    print(index, course)
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
for index,courses in enumerate(courses, start=1): #To start index from 1 instead of 0
    print(index, courses)
"""


"""
courses = ['History', 'Mathematics', 'Physics', 'CompSci']
courses_str = ', '.join(courses) #To convert list into string
print(courses_str)  
courses_strg = '-'.join(courses)#To add - between elements
print(courses_strg)
"""


"""
#Mutable
list_1 = ['History', 'Mathematics', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
 
list_1[0]= 'Art'
print(list_1)
print(list_2)
"""

"""
#Immutable
tuple_1 =('History', 'Mathematics', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)  

tuple_1[0] = 'Art' #TypeError: 'tuple' object does not support item assignment
print(tuple_1)
print(tuple_2)
""" 


# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)


cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} #Sets throw away duplicates
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print('Math' in cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.union(art_courses))






