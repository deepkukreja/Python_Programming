class Customer:

    def __init__(self, name):
        self.name = name


cust = Customer("Deep")
print(cust.name)




class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")


cust = Customer("Ankita", "Female")
greet(cust)







class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")

    cust2 = Customer("Deep_Kukreja", "Male")
    return cust2


cust = Customer("Ankita", "Female")

new_cust = greet(cust)
print(new_cust.name)









class Customer:

    def __init__(self, name):
        self.name = name


def greet(customer):
    print(id(customer))
    customer.name = "Deep"
    print(customer.name)
    print(id(customer))


cust = Customer("Ankita")
print(id(cust))

greet(cust)

print(cust.name)

# class ke objects are also mutable like lists, dict and sets










def change(L):
    print(id(L))
    L.append(5)
    print(id(L))


L1 = [1, 2, 3, 4]
print(id(L1))
print(L1)

change(L1)

print(L1)











def change(L):
    print(id(L))
    L = L + (5, 6) 
    print(id(L))

L1 = (1, 2, 3, 4)
print(id(L1))
print(L1)

change(L1)

print(L1)
