class ATM:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.__menu()

    # private menu
    def __menu(self):
        while True:
            user_input = input("""
Hello, how would you like to proceed?
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit
""")

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid choice")

    # public methods
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfully")

    def deposit(self):
        if self.__validate_pin():
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")

    def withdraw(self):
        if self.__validate_pin():
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Operation successful")
            else:
                print("Insufficient funds")

    def check_balance(self):
        if self.__validate_pin():
            print("Balance:", self.__balance)

    # private pin validation
    def __validate_pin(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.__pin:
            return True
        print("Invalid pin")
        return False

    # getter
    def get_pin(self):
        return "Not allowed"

    # setter
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("Not allowed")


atm = ATM()

