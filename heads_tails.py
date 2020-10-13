import random
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

