nums = [2, 5, 8, 1, 4, 7, 10]
even = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
print(even)




# Using filter() function
nums = [2, 5, 8, 1, 4, 7, 10]

def is_even(n):
    return n % 2 == 0
even = list(filter(is_even, nums))
print(even)



nums = [2, 5, 8, 1, 4, 7, 10]
even = list(filter(lambda n: n % 2 == 0, nums))
print(even)
