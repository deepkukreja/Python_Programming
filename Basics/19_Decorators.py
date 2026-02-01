def divide(a,b):
    if a<b:
        a,b = b,a
    return a/b

def subtract(a,b):
    if a<b:
        a,b = b,a
    return a-b

print(divide(2,8))  # Output: 4.0
print(subtract(2,8))  # Output: 6




def log_deco(func):
    def wrap(*args, **kwargs):
        print("v# alues", args)
        result = func(*args)
        print("Result", result)
        return result
    return wrap



def greater_first(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap

# Decorators are functions that take another function as input and extend its behavior without modifying it directly.

@log_deco
@greater_first
def divide(a, b):
    return a / b


@log_deco
@greater_first
def sub(a, b):
    return a - b


@log_deco 
def add(a, b, c):
    return a + b + c


# -------------------------
# Function calls
# -------------------------
divide(8, 20)
sub(2, 4)
add(5, 7, 6)
