
import sys
import random
from enum import Enum

class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3


playerchoice = input(f"Enter...\n1 For Rock,\n2 For paper, \n3 For scissors\nPlay: ")
player = int(playerchoice)


if player < 1 or player > 3:
    sys.exit ("you have to chose between 1, 2, or 3.")

computerchoice = random.choice(["1","2","3"])
computer = int(computerchoice)


print("you chose " + str(RPS(player)).replace('RPS', '') + ".")
print("computer chose " + str(RPS(computerchoice)).replace('RPS', '') + ".")



if player == 1 and computer == 3:
  print("😊You win!")
elif player == 2 and computer == 1:
  print("😊You win!")
elif player == 3 and computer == 2:
  print("😊You win!")
elif player == computer:
  print("😲Tie game!")
else:
  print("computer win!")
