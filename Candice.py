import math
import random

print("Hello, I am Candice the Helper bot.\n")
print("Answer all questions with a yes or no.\n")
print("I can perform the following functions-\n")
print("[1] Mathematical Calculation")
print("[2] Data Entry")
print("[3] Guessing Game")
print("[4] Number Converter")
print("[5] Heads/Tails decider")


def mat(x,y,z):
    if z == "+":
        add = x+y
        return add
        
    elif z == "-":
        minus = x-y
        return minus
        
    elif z == "*":
        product = x*y
        return product
    elif z == "**":
        a = a=float(input(f'Raise {x} or {y}? '))
        b = int(input("Select power: "))
        if a == x:
            power1 = x**b
            return power1
        elif a == y:
            power2 = y**b
            return power2
            
            
    elif z == "/":
        divide = x/y
        return divide
    
    elif z == "sqrt":
        ask = float(input(f'Root of {x} or {y}? '))
        if ask == x:
            sqrtx = math.sqrt(x)
            return sqrtx
        
        elif ask == y:
            sqrty = math.sqrt(y)
            return sqrty
        
        
a1 = int(input("Enter the function you wish to operate: "))
print("\n")
if a1 == 1:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = input("Enter the operator: ")
    
    rio = mat(x,y,z)
    print(rio)

dict1 = {}
if a1 == 2:
    dataname = input("Enter the database name you wish to create: ")
    i=0
    limit = int(input("Enter the limit of the database: "))

    while i <= limit:
        i=i+1
        entry = input("Enter your entry: ")
        a = input("Enter entry ")
        d = input("Select name of key: ")
        check = input("Would you like to go within the database for nesting? ").strip().capitalize()
        if check == "Yes":
            b = input("Enter entry: ")
            c = input("Select name of key: ")
            dict1 = {entry:{d:a, c:b}}
            
        elif check == "No":
            break
        
        check = input("Would you like to see your database? ").strip().capitalize()
        if check == "Yes":
            print(dict1)
            
        elif check == "No":
            break
        
if a1 == 3:
    print("Welcome to the guessing game!\n")
    print("This is a rudimentary game to pass some time.\n")
    rules = input("Would you like to know the rules to the game? ").strip().capitalize()
    if rules == "Yes":
        print("\n")
        print("First, you will choose an upper and lower limit for which the guessing game will operate\n")
        print("The Program will then ask you to select a number from your keyboard.\n")
        print("If the number you chose is one of the number chosen by the computer, you win.\n")
        print("Higher is the range of the two limits, more difficult it gets.\n")
        
    upper = int(input("Choose the upper limit: "))
    lower = int(input("Choose the lower limit: "))
    while True:
        comp = random.randint(lower,upper)
        enter = int(input("Enter your guess! "))
        if comp == enter:
            print("Wow, you win!")
            again = input("Would you like to play again? ").strip().capitalize()
            if again == "Yes":
                continue
            
            elif again == "No":
                break
            
        if enter > comp:
            print("Oops, you went above the number chosen by the computer ")
            again = input("Would you like to play again? ").strip().capitalize()
            if again == "Yes":
                continue
            
            elif again == "No":
                break
            
        if enter < comp:
            print("Oops, you went under the number chosen by the computer ")
            again = input("Would you like to play again? ").strip().capitalize()
            if again == "Yes":
                continue
            
            elif again == "No":
                break
            
def conv(x,types):
     if types == "Octal":
        type1 = oct(x)
        return type1
    
     elif types == "Binary":
         type2 = bin(x)
         return type2
    
     elif types == "Hexadecimal":
         type3 = hex(x)
         return type3
    
if a1 == 4:
    x = int(input("Enter decimal number to be converted: "))
    types = input("Enter the type you want to convert to: ").strip().capitalize()
    
    ans = conv(x,types)
    print(ans)
    
if a1 == 5:
    choices = ["Heads","Tails"]

    def rev(a,b,c,d):
        select = random.choice(choices)
        if b == select and d != select:
            result1 = (a, "has won")
            return result1
        
        elif d == select and b != select:
            result2 = (c, "has won")
            return result2

    while True:
        a = input("Enter p1  name: ").strip().capitalize()
        b = input("Enter your choice: ").strip().capitalize()
        c = input("Enter p2 name: ").strip().capitalize()
        d = input("Enter your choice: ").strip().capitalize()
        print(rev(a,b,c,d))
        ask = input("Would you like to play again? ").strip().capitalize()
        if ask == "Yes":
            continue
        elif ask == "No":
            break
    
    print("Thanks for playing!")
