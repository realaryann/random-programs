a = {
    "Aryan":{"9th":56, "10th":80, "11th":100,"12th":90},
    "Swapnil":{"9th":70, "10th":40,"11th":90,"12th":97},
    "Akshat":{"9th":95, "10th":45, "11th":95,"12th":80},
    "Ayaan":{"9th":50, "10th":30,"11th":80,"12th":70},
    "Rohit":{"9th":40, "10th":50, "11th": 76,"12th":94}
    }

a1 = ["Aryan", "Swapnil","Akshat","Ayaan","Rohit"]

#if name is in pre defined dict
print("-----------------Hello, and welcome to Highschool marks database----------------")
r = input("Please select a name: ").strip().capitalize()
if r in a1:
    print("Great! the name you entered is in the database! ")
    t = input("Please select a further class whose marks you wish to view: ").strip().capitalize()
    print(a[r][t])
    
#if name is not in pre defined dict   
else:
    j = input("The name you entered is not in the list, would you like to register them?(yes/no) ").strip().capitalize()
    if j == "Yes":
        q = input("Enter your name: ").strip().capitalize()
        y = input("Enter your marks in 9th: ")
        z = input("Enter your marks in 10th: ")
        u = input("Enter your marks in 11th: ")
        v = input("Enter your marks in 12th: ")
        b = {q:{"9th":y,"10th":z, "11th":u, "12th":v}}
        print("Great! the records have now been saved in the database! ")
        #To register repeated people in new dictionary
        while True:
            l = input("Would you like to register another person in the high school database?(yes/no): ").strip().capitalize()
            if l == "Yes":
                w = input("Enter your name: ").strip().capitalize()
                s = input("Enter your marks in 9th: ")
                o = input("Enter your marks in 10th: ")
                g = input("Enter your marks in 11th: ")
                t = input("Enter your marks in 12th: ")
                b[w]={"9th":s, "10th":o, "11th":g, "12th":t}
             
            elif l == "No":
                break
        
   #repeated actions to display data 
    while True:   
        k = input("Enter the name you want to look up: ").strip().capitalize()
        if k in b:
            y = input("Enter the class: ")
            print(b[k][y])
    
        elif k in a:
            y = input("Enter the class: ")
            print(a[k][y])
        #option to keep on searching for new candidate/student    
        i = input("Would you like to continue?(yes/no) ").strip().capitalize()
        if i == "Yes":
            continue
        elif i =="No":
            break
print("Thanks for using the highschool database")
