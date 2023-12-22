from game import display
from game import display_user_input
from game import computers_turn
from game import win_check
import random

#Find a fix for 5th computer turn, since it breaks the program
print('WELCOME TO THE FRANKENSTEINS TIC TAC TOE GAME!!')
display()
moves_left = 5
while moves_left >= 0:
    display_user_input()
    computers_turn()
    if win_check() == True:
        break

    moves_left -= 1



