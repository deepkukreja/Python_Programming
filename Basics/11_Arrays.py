# ------------------------------------------------------------
# TypeCode | C Type           | Python Type        | Min size (bytes)
# ------------------------------------------------------------
# 'b'      | signed char      | int                | 1
# 'B'      | unsigned char    | int                | 1
# 'u'      | Py_UNICODE       | Unicode character  | 2
# 'h'      | signed short     | int                | 2
# 'H'      | unsigned short   | int                | 2
# 'i'      | signed int       | int                | 2
# 'I'      | unsigned int     | int                | 2
# 'l'      | signed long      | int                | 4
# 'L'      | unsigned long    | int                | 4
# 'f'      | float            | float              | 4
# 'd'      | double           | float              | 8
# ------------------------------------------------------------




from array import *
arr1 = array ('i', [33, 4, 55, 6, 88])
print(arr1)
print(arr1.tolist())
print(arr1.buffer_info())
for n in arr1:
    print(n)



from array import *
arr1 = array ('i', [33, 4, 55, 6, 88])
arr1.append(77)
for n in arr1:
    print(n)



from array import *
arr1 = array ('i', [33, 4, 55, 6, 88])
arr1.reverse()
for n in arr1:
    print(n)



from array import *
arr1 = array('i', [33, 4, 55, 5, 66])
arr2 = arr1
print(arr1)
print(arr2)



from array import *
arr1 = array('i', [33, 4, 55, 5, 66])
arr2 = array('i', arr1.tolist())
arr1[2] = 54
print(arr1)
print(arr2)



from array import *
arr1 = array('i', [33, 4, 55, 5, 66])
arr2 = array(arr1.typecode, arr1.tolist()) # Using typecode ensures arr2 has the SAME data type as arr1
arr1[2] = 54
print(arr1)
print(arr2)




from array import *
arr1 = array('i', [33, 4, 55, 5, 66])
arr2 = array(arr1.typecode, (n for n in arr1))  # (n for n in arr1) → copies each element one by one
arr1[2] = 54
print(arr1)   
print(arr2) 

