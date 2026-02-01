def outer():
    print("Outer function")
    def inner(num):
        print("Inner function", num)
    return inner
something = outer()
something(10)

# Whats happening here?
# 1. The outer function is defined and called, which prints "Outer function".
# 2. The inner function is defined within the outer function but not called yet.
# 3. The outer function returns the inner function object.
# 4. The returned inner function is assigned to the variable 'something'.   
# 5. When 'something(10)' is called, it invokes the inner function with the argument 10, printing "Inner function 10".

