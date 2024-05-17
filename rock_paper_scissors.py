import random

def main():
    score_pc = 0
    score_user = 0

    while True:
        user_choice = input("rock-paper-scissor? ").lower()
        n= random.randint(1,2)
        if n==1:
            pc_choice = pc_choice_func()
        else:
            pc_choice = pc_tip_choice(user_choice)
        print("PC choice:", pc_choice)

        if pc_choice == user_choice:
            print("It's a tie!")
        elif (pc_choice == "rock" and user_choice == "paper") or \
             (pc_choice == "paper" and user_choice == "scissor") or \
             (pc_choice == "scissor" and user_choice == "rock"):
            score_user += 1
        else:
            score_pc += 1

        print("YOUR SCORE: ", score_user, "vs. PC SCORE: ", score_pc)

        if score_user == 3 or score_pc == 3:
            break

    if score_pc == 3:
        print("PC WON THE GAME")
    if score_user == 3:
        print("YOU WON THE GAME")


def pc_tip_choice(user_choice):

    if user_choice == "rock":
        return "paper"
    if user_choice == "paper":
        return "scissor"
    if user_choice == "scissor":
        return "rock"



def pc_choice_func():
    n = random.randint(1, 3)
    if n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissor"  
    
if __name__ == "__main__":
    main()


