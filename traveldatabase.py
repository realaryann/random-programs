import math
import random
import time
import pickle

with open("Upass.dat","wb") as fp:
    bflights=[]
    airports = {"Delhi":"Indira Gandhi Airport","Kolkata":"Netaji Subhash Chandra Bose International Airport","Mumbai": "Chhatrapati Shivaji Maharaj International Airport"}
    B= [[1,"IND-CANADA"],[2,"IND-DUBAI"],[3,"IND-SINGAPORE"],[4,"IND-B"]]
    fhistory = []
    L=[["aryannagpal27","hello123"],["aarush90","numkey123"],["daksh23","keykey23"]]
    pickle.dump(L,fp)
    
def portal(fhistory,B,airports):
                    
                    print("welcome to X Travel Profile portal")
                    print("Following are the options for the portal: ")
                    print("[1] Book a flight (Requires flight code)")
                    print("[2] check flight history")
                    print("[3] Check available flights and flight codes: ")
                    print("[4] Check nearest airports")
                    print("[5] Flight Cancellation") 
                    print("\n")
                    ask = int(input("Enter the number for the services shown above: "))
     
                    if ask == 3:
                        for x in B:
                            print(x)
                        ask2 = int(input("Enter the flight number you are interested in booking: "))
                        print("You have chosen", B[ask2],"This flight is added in your  flight history")
                        fhistory.append(B[ask2])
                        print("/n")
                        portal(fhistory,B,airports)
                        
                    elif ask == 1:
                        print("Would you like to book the flight from your flight history? ")
                        print("Your flight history is\n")
                        for i in fhistory:
                            print(i)
                        member = int(input("Enter the number of people to be travelling: "))
                        class1 = input("Would you like to choose economy (e) or premium (p)")
                        cred = [member,class1]
                        bflights.append(cred)
                        print("Your final flight details are ", cred)
                    elif ask == 2:
                        print("Your flight history is: ", fhistory)
                        portal(fhistory,B,airports)
                    elif ask == 4:
                        print(airports)
                        agane = input("Would you like to reboot the portal? (y/n): ")
                        if agane == "y":
                            portal(fhistory,B,airports)
                    elif ask == 5:
                        print("This window is used to remove any booked flights")
                        print("Your current booked flight is ", bflights)
                        fask = input("Would you like to cancel this flight? (It will put a strike on your account) : ")
                        if fask == "y":
                            bflights.clear()
                        
                            

with open("Upass.dat","rb") as g:
    L2 = pickle.load(g)
    print("Welcome to X Travel agency service")
    print("Please sign in the terminal or sign up to access the terminal: ")
    print("Please respond to each question with a y or n")
    ask1 = input("Do you have a previous account in the system manager? : ")
    if ask1 == "y":
        userid1 = input("Enter your userid: ")
        passw1 = input("Enter your password: ")
        for i in L:
            if i[0] == userid1:
                 portal(fhistory,B,airports)
                        
                
    if ask1 == "n":
        acc1 = input("Would you like to create an account?: ")
        if acc1 == "y":
            user = input("Enter your username: ")
            passw = input("Enter your password: ")
            K = [user,passw]
            B.append(K)
            print("Congratulations! Your account has been created.")
            ask3 = input("Would you like to start the portal? ")
            if ask3 == "y":
                portal(fhistory,B,airports)
    
