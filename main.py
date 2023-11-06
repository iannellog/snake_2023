"""
Created on Sept. 29, 2023
by Giulio Iannello
"""

from snake import Snake
from play_field import Play_field

# Snake game

height = 10
width = 10
obstacles = []
food = []
# get layout and moves
# create snake object (including an empty initial tail)
snake = Snake()
# create play field object
play_field = Play_field(height, width, obstacles, food)
# put snake in start position
# for m in moves:
#    check if move is valid for play filed; if it is, return the new head position and if it contains food
#    if move is valid:
#        check if new position is valid for the snake, taking into account if it eats food
#        if new position is valid:
#            update play field
#            update snake (including its tail)
#    if move is not valid:
#        break
# display play field and snake (including its path)

