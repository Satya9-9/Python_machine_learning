import random
def get_choices():
    player_choice = input("enter the choice of the player (Rock, Paper, Scissor) ")
    option = ["rock", "paper","scissors"]
    computer_choice = random.choice(option)
    choices =  {'player': player_choice, "computer":computer_choice}
    return choices 
print(get_choices())