class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13)
print(s.brand)











class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand   # private variable
        self.camera = camera


class SmartPhone(Phone):
    pass
    # Child class cannot directly inherit/access
    # parent class PRIVATE members (__brand)


s = SmartPhone(20000, "Apple", 13)
print(s._Phone__brand)  
# accessing private variable using name mangling











class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand   # private variable
        self.camera = camera


class SmartPhone(Phone):
    pass
    # Child class cannot directly inherit/access
    # parent class PRIVATE members (__brand)


s = SmartPhone(20000, "Apple", 13)
print(s._Phone__brand)  
# accessing private variable using name mangling
s._Phone__brand = "Samsung"  # changing private variable using name mangling
print(s._Phone__brand)













class Parent:

    def __init__(self, num):
        self.__num = num   # private variable

    def get_num(self):
        return self.__num


class Child(Parent):

    def show(self):
        print("This is in child class")
        # Child class CANNOT directly access parent class
        # private members (__num)


son = Child(100)

print(son.get_num())   # accessing private data via parent method
son.show()








class Parent:

    def __init__(self, num):
        self.__num = num   # private variable

    def get_num(self):
        return self.__num


class Child(Parent):

    def __init__(self, val, num):
        self.__val = val
        # Parent constructor is NOT called automatically
        # when child defines its own __init__()
        super().__init__(num)

    def get_val(self):
        return self.__val


son = Child(100, 10)

print("Parent Num:", son.get_num())
print("Child Val:", son.get_val())












class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()   # calling parent class method


s = SmartPhone(20000, "Apple", 13)
s.buy()




















class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("class A:", self.var1)


class B(A):
    def display2(self, var1):
        print("class B:", self.var1)


obj = B()
obj.display1(200)



















class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("Pehle yahan")
        super().__init__(price, brand, camera)  # call parent constructor
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")


s = SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)










class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)   # calling parent constructor
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 200)

print(son.get_num())
print(son.get_val())










class Parent:

    def __init__(self):
        self.num = 100


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)


son = Child()
son.show()









class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent:", self.__num)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print("Child:", self.__var)


dad = Parent()
dad.show()

son = Child()
son.show()








################################ Example of Single level inheritance ################################

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()













################################ Example of Multilevel Inheritance ################################

class Product:
    def review(self):
        print("Product customer review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
s.return_phone()










############################### Hierarchical Inheritance ###############################

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


# Child class 1
class SmartPhone(Phone):
    pass


# Child class 2
class FeaturePhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()









############################### Multiple Inheritance ###############################

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def review(self):
        print("Customer review")


# Child class inheriting from MULTIPLE parent classes
class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)

s.buy()
s.review()



















############################### MRO example ###############################

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def buy(self):
        print("Product buy method")


# Multiple inheritance with MRO
class SmartPhone(Product, Phone):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()











############################### Example 1 on Types ###############################

class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        return 30

    def m2(self):
        return 40


class C(B):
    def m2(self):
        return 20


obj1 = A()
obj2 = B()
obj3 = C()

print(obj1.m1() + obj3.m1() + obj3.m2())










############################### Example 2 ###############################

class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        val = super().m1() + 30
        return val


class C(B):
    def m1(self):
        val = self.m1() + 20   # ❌ problem here
        return val


obj = C()
print(obj.m1())
