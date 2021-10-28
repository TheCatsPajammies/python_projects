def greet(bot_name, birth_year): 
    print("Hello, my name is " + bot_name + ".")
    print("I was created in " + birth_year + ".")

def name_intro():
    print("What's your name, br0ether?")
    name = input()
    print("That's a siiiiiiick name you have,", name + "!")

def guess_age():
    print("I bet I can guess your age.")
    print("Enter remainders of dividing your age by 3, 5, and 7.")

    remainder_3 = int(input())
    remainder_5 = int(input())
    remainder_7 = int(input())

    age = ((remainder_3 * 70) + (remainder_5 * 21) + (remainder_7 * 15)) % 105

    print("You're", age, "years young; that's a great time to start programming!")

def count():
    print("Now I'm gonna prove to you that I can count to any number you want!")
    your_number = int(input())
    
    i = 0
    while i <= your_number:
        print(str(i) + "!")
        i += 1

def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    
    answer = input()

    while answer != "2":
        if answer == "2":
            print("Hell yeah, br0ether!")
        else:
            print("Incorrect, broether! Try again!")
            answer = input()
    print("You did it, br0ether!")

def end():
    print("Have a radical day, br0ether! I love you!")

greet("Tank", "2020")
name_intro()
guess_age()
count()
test()
end()