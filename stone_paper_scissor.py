import random
choices = ["Stone","Paper","Scissor"]

def rev(name1,choice1):
    compchoice = random.choice(choices)
    if choice1 == compchoice:
        result1 = (f'It is a tie round')
        return result1
    
    elif choice1 == "Stone" and compchoice == "Paper":
        result2 = (f'Oh.. the computer chose paper, {name1} loses')
        return result2
        
    elif choice1 == "Stone" and compchoice == "Scissor":
        result3 = (f'Yay, the computer chose scissor, {name1} wins')
        return result3
        
    elif choice1 == "Scissor" and compchoice == "Stone":
        result4 = (f'Oh.. the computer chose stone, {name1} loses')
        return result4
        
    elif choice1 == "Scissor" and compchoice == "Paper":
        result5 = (f'Yay, the computer chose paper, {name1} wins')
        return result5
        
    elif choice1 == "Paper" and compchoice == "Stone":
        result6 = (f'Yay, the computer chose stone, {name1} wins')
        return result6
        
    elif choice1 == "Paper" and compchoice == "Scissor":
        result7 = (f'Oh.. the computer chose scissor, {name1} loses')
        return result7

while True:
    name1 = input("What is your name? ").strip().capitalize()
    choice1 = input("What is your choice? ").strip().capitalize()
    print(rev(name1,choice1))
    ask = input("Would you like to play again? ").strip().capitalize()
    if ask == "Yes":
        continue
    
    elif ask == "No":
        break
    
    elif ask not in "YesNo":
        print("It was a yes/no question dummy")
        break