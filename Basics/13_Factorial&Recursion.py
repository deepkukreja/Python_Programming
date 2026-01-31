def fact(num):
    res = 1

    for i in range(1, num+1):
        res = res*i

    return res
    
result = fact(5)
result = fact(100)
print(result)


"""
import sys  # sys module provides access to Python runtime and system-level operations
from time import sleep
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

count = 1

def greet():
    global count
    print("Hello", count)
    count = count + 1
    sleep(.02)
    greet()

greet()
"""



def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)

result = fact(8)
print(result)