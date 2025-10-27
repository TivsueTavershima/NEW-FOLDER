print('')
import random
import sys
from enum import Enum
class RPS(Enum):
      ROCK = 1
      PAPER =2
      SCISSORS = 3

playerchoice = input('1.rock, \n2.paper,\n3.scissors\nplease make your chioce: ')

player = int(playerchoice)

if playerchoice < '1' or playerchoice > '3':
  sys.exit('you must enter 1,2,or 3')
  
computerchoice = random.choice("123")
computer = int(computerchoice)

print('you chose: '+ str(RPS(player)).replace('RPS','') +',')
print('Taver chose: '+ str(RPS(computer)).replace('RPS','') +',')

if player == 1 and computer == 3:
  print('you win!')
elif player == 2 and computer == 1:
  print('you win!')
elif player == 3 and computer == 2:
  print('you win!')
elif player == computer:
  print('Tie game!')
else:
  print('Taver wins!')