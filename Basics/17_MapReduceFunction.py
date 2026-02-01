nums = [4,2,8,9,7,5,2,3,6,1]

def double_it(n):
    return n * 2

evens = filter(lambda n: n % 2 == 0, nums)
double_it=list(map(double_it, evens)) # map function is used to double each even number

print(double_it)


from functools import reduce
nums = [4,2,8,9,7,5,2,3,6,1]


evens = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n * 2, evens))
sum_of_doubles = reduce(lambda a, b: a + b, double) #reduce function is used to sum all the doubled values

print(evens)
print(double)
print(sum_of_doubles)


