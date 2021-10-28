class CoffeeMachine:
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def buy(self):
        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:\n")
        if drink == "1":
            if self.water >= 250 and self.coffee_beans >= 16:
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if self.water < 250:
                    print("Sorry, not enough water!\n")        
                elif self.coffee_beans < 16:
                    print("Sorry, not enough coffee beans!\n")
                
        if drink == "2":
            if self.water >= 350 and self.coffee_beans >= 20 and self.milk >= 75:
                self.water -= 350
                self.coffee_beans -= 20
                self.milk -= 75
                self.money += 7
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if self.water < 350:
                    print("Sorry, not enough water!\n")
                elif self.coffee_beans < 20:
                    print("Sorry, not enough coffee beans!\n")
                elif self.milk < 7:
                    print("Sorry, not enough milk!\n")
        if drink == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 200:
                print("Sorry, not enough water!\n")
            elif self.coffee_beans < 12:    
                print("Sorry, not enough coffee beans!\n")
            elif self.milk < 100:    
                print("Sorry, not enough milk!\n")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add?:\n")) 
        self.milk += int(input("Write how many ml of milk do you want to add?:\n")) 
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add?:\n"))
        self.disposable_cups += int(input("Write how many disposaple cups of coffee do you want to add?:\n"))
        

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def remaining(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.disposable_cups} of disposable cups\n{self.money} of money\n".format())
    
    def coffee_machine(self):
        while True:
            choice = input("Write action (buy, fill, take, remaining, exit):\n")
            if choice == "buy":
                self.buy()
            elif choice == "fill":
                self.fill()
            elif choice == "take":
                self.take()
            elif choice == "remaining":
                self.remaining()
            elif choice == "exit":
                exit()

coffeemachine = CoffeeMachine()
coffeemachine.coffee_machine()




    