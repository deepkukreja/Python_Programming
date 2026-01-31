def square(num):
    return num*num
def cube(num):
    return num * num * num

def operate(num, operation):

    return operation(num)   #square num
value = 5
result = operate(value, square)
print(result)





def square(num):
    return num*num
def cube(num):
    return num * num * num

def operate(nums, operation):
   
    for i in nums:
        result = operation(i)
        print(result)

nums = [5, 6, 7]
operate(nums, cube)