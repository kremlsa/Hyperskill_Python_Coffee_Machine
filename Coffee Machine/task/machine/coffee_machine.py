class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.balance = 550
        self.state = "waiting"

    def fill_water(self, operation):
        self.water += operation

    def fill_milk(self, operation):
        self.milk += operation

    def fill_beans(self, operation):
        self.beans += operation

    def fill_cups(self, operation):
        self.cups += operation

    def get_status(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.balance))
        print()
        self.state = "waiting"

    def buy_espresso(self):
        if self.check_resource(250, 0, 16, 1):
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.balance += 4
            print("I have enough resources, making you a coffee!")
            print()
        self.state = "waiting"

    def buy_latte(self):
        if self.check_resource(350, 75, 20, 1):
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.balance += 7
            print("I have enough resources, making you a coffee!")
            print()
        self.state = "waiting"

    def buy_cappuccino(self):
        if self.check_resource(200, 100, 12, 1):
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.balance += 6
            print("I have enough resources, making you a coffee!")
            print()
        self.state = "waiting"

    def check_resource(self, w, m, b, c):
        if self.water < w:
            print("Sorry, not enough water!")
            print()
            return False
        if self.milk < m:
            print("Sorry, not enough milk!")
            print()
            return False
        if self.beans < b:
            print("Sorry, not enough coffee beans!")
            print()
            return False
        if self.cups < c:
            print("Sorry, not enough cups!")
            print()
            return False
        return True

    def buy(self, operation):
        if operation == "1":
            self.buy_espresso()
        if operation == "2":
            self.buy_latte()
        if operation == "3":
            self.buy_cappuccino()
        if operation == "back":
            self.state = "waiting"

    def get_balance(self):
        print("I gave you ${}".format(self.balance))
        print()
        self.balance = 0
        self.state = "waiting"

    def menu(self, operation):
        if operation == "buy":
            self.state = "buying"
        if operation == "fill":
            self.state = "fill_water"
        if operation == "take":
            self.get_balance()
        if operation == "remaining":
            self.get_status()
        if operation == "exit":
            self.state = "stopping"

    def fill(self, operation):
        if self.state == "fill_water":
            self.fill_water(int(operation))
            self.state = "fill_milk"
        elif self.state == "fill_milk":
            self.fill_milk(int(operation))
            self.state = "fill_beans"
        elif self.state == "fill_beans":
            self.fill_beans(int(operation))
            self.state = "fill_cups"
        elif self.state == "fill_cups":
            self.fill_cups(int(operation))
            self.state = "waiting"

    def process_input(self, operation):
        if self.state == "waiting":
            self.menu(operation)
        elif self.state == "buying":
            self.buy(operation)
        elif self.state.startswith("fill_"):
            self.fill(operation)

    def get_state(self):
        if self.state == "waiting":
            print("Write action (buy, fill, take, remaining, exit):")
        if self.state == "buying":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.state == "fill_water":
            print("Write how many ml of water you want to add:")
        if self.state == "fill_milk":
            print("Write how many ml of milk you want to add:")
        if self.state == "fill_beans":
            print("Write how many grams of coffee beans you want to add:")
        if self.state == "fill_cups":
            print("Write how many disposable coffee cups you want to add")


my_coffee_machine = CoffeeMachine()
while not my_coffee_machine.state == "stopping":
    my_coffee_machine.get_state()
    my_coffee_machine.process_input(input())
