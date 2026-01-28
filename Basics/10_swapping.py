a= 5
b= 6

#Method 1
c = a
a = b
b = c
print("a : ",a)
print("b : ",b)


#Method 2
a = a+b #a here becomes 11
b = a-b #b here becomes 11-6=5
a = a-b #a here becomes 11-5=6
print("a : ",a)
print("b : ",b)


#Method 3
a = a^b
b = a^b
a = a^b
print("a : ",a)
print("b : ",b)


#Method 4 (easiest)
a,b = b,a  #In backend, tupple packing and unpacking happens so it's not overwritting a and b
print("a : ",a)
print("b : ",b)