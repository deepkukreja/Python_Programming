nums = [1, 2, 3, 4, 5]  
for num in nums:
 print(num)



nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!!")
        break
    print(num)



nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!!")
        continue
    print(num)



nums = [1, 2, 3, 4, 5]
for num in nums:
   for letters in 'abc': #In this loop, each number will be assigned to each letter like 0a, 0b, 0c, 1a, 1b and so on upto 5c
      print(num, letters)



for i in range(10): #It will print from 0 to 9 
   print(i)



for i in range(1, 11): #To print numbers from 1 to 10
  print(i)



x = 0
while x < 10:
  print(x)
  x+=1


x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x+=1



x=0
while True:
  #if x==5:
   # break
  print(x)
  x+=10


 i = 1
while i <=5:
    print("Deep", end = "")
    j = 1
    while j <=4:
        print("Rocks!!!", end = "")
        j+=1
    
    i+=1
    print()  #For new line
print(i)




# 1. Iterating over a range of numbers
print("Iteration using range():")
for i in range(1, 6):
    print(i)

print("-" * 20)

# 2. Iterating over a list
fruits = ["apple", "banana", "mango"]
print("Iteration over a list:")
for fruit in fruits:
    print(fruit)

print("-" * 20)

# 3. Iterating over a string
word = "Python"
print("Iteration over a string:")
for char in word:
    print(char)

print("-" * 20)

# 4. Using for loop with break and continue
print("Using break and continue:")
for num in range(1, 11):
    if num == 5:
        continue  # skips 5
    if num == 9:
        break     # stops loop at 9
    print(num)

