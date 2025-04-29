import random
import time
user_wins = 0
comp_win = 0
draw = 0
choice = ["rock", "paper", "scissors"]

while True:
    start_time = time.time()
    user_input = input("Pick one: Rock/Paper/Scissors or Q: ").lower()
    if user_input == "q":
        break
    
    if user_input not in choice:
        continue

    random_input= random.randint(0,2)
    comp_pick = choice[random_input]
    print("Computer picks :", comp_pick)
    '''
   if user_input == "rock" and comp_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("Computer won!")
        comp_win += 1. 
        '''
    if ((user_input == "rock" and comp_pick == "scissors") or
       (user_input == "paper" and comp_pick == "rock") or
       (user_input == "scissors" and comp_pick == "paper")):
        print("You won!")
        user_wins += 1
    elif user_input == comp_pick:
        print("Draw!")
        draw += 1
    else:
        print("Computer won!")
        comp_win += 1
    
    end_time = time.time()
    time_taken = end_time - start_time
    
print("You got", user_wins, "wins")
print("Comp got",comp_win,"wins")
print("There were", draw, "ties")
print(f"Time taken to play: {time_taken} seconds")