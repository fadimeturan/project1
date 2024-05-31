import random

def roll():
    min= 1
    max= 6
    roll = random.randint(min, max)

    return roll


while True:
    players= int(input("Enter the number: "))
    if 1<= players <=4:
        break
    else:
        print("Must be between 2-4 players.")
    

max_score= 50
players_scores= [0 for i in range(players)]

while max(players_scores) < max_score:

    for player in range(players):
        print(f"\nPlayer number {player +1} turn has just started!\n")
        print(f"Your total score is: {players_scores[player]}\n")

        current= 0
        
        while True:
            option= input("would you like to roll (y/n)? ").lower()
            if option.lower() != "y":
                break

            value= roll()
            if value ==1:
                print("You rolled a 1! Turn done!")
                current = 0
                break

            else:
                current += value
                print(f"You rolled a: {current}")
            
            print(f"Your score is: {current}")
    
        players_scores[player] += current
        if players_scores[player] >= max_score:
                  break
        
max_score = max(players_scores)
winning= players_scores.index(max_score)
print(f"Player number {winning +1} is the winner with a score of: {max_score}")