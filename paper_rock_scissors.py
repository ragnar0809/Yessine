import random
from random import choice
Game = ["Rock", "Paper", "Scissors"]
computer_game = random.choice(Game)
player_game = str(input("Rock , Paper or Scissors: "))
if player_game not in Game:
	print("Error")
elif computer_game == player_game:
        print("Draw")
elif computer_game == "Rock" and player_game == "Paper":
        print(computer_game, " " "Booyah")
elif computer_game == "Paper" and player_game == "Scissors":
        print(computer_game, "", "Booyah")
elif computer_game == "Scissors" and player_game == "Rock":
        print(computer_game, "Booyah")
else:
        print(computer_game, "", "You Lost")
    
    
