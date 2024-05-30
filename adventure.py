
name= input("What is your name? ")
print(f"Welcome {name}! Let's start!")

answer= input("You are 20 and you can go to a great collage or start world tour with pretty little money? Choose: collage or world tour? ").lower()

if answer == "collage":
    print("Congrats! Now you are 25 and work at international company, make $15000 monthly! You are thinking about starting up your own bussiness. However, it could either collapsed or it be tough for a couple of years making money more than current company. WHat would you do: stay or start up?")
    
    choice1 = input().lower()
    if choice1 == "stay":
        print("You worked in same company for 7 years and had great promotions. You save your money and now you have your own bussines with 23 employee! And you are happy!")
    elif choice1 == "start":
        print("Because of your insufficient experiences your start up journey was a huge fail! You are in debt.")
    else:
        ("Not a valid choice.")

elif answer == "world tour":
    print("Welcome to the broooooke era. Okey just kidding. The last 4 years was incredible and unbelievable for you with thousands of experiences. You also shared videos on the way and earned money from social media! Now you are tired and think about moving France or Italy: choose one!")
    
    choice2 = input().lower()
    if choice2 == "France":
        print("You died in a horrible train accident on the way. Rest in peace, my dear. You can continue your journey in from heaven I hope.")

    elif choice2 == "Italy":
        print("You are living your best life in Amalfi. You have a crush for a while. Do you want to marry: yes or no?")

        choice3 = input().lower()
        if choice3 == "yes":
            print("Marriege was not good for you. You stood for a long time in a mental clinic to be okey again after a fantastic divorce.")

        elif choice3 == "no":
            print("You died alone.")
        
        else:
            ("Not a valid choice.")

    else:
        ("Not a valid choice.")

else:
    ("Not a valid choice.")
