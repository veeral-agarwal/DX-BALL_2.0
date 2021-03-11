import config
import random
from time import sleep, time

from colorama import init, Fore, Back, Style
init()
import global_variables

class Board():

    height = int(config.rows)
    length = int(config.columns)

    def __init__(self):
        self.begin_time = time()
        self.matrix = [[ " " for i in range(self.length)] for j in range(self.height) ] 
        self.border()
        
    def render(self):
        global_variables.total_time = time()-self.begin_time
        print("you have 200 seconds in game and 5 lives.")
        print(" 'q' for quit , 'a' and 'd' for moving paddle left and right resp. , 'x' for shoot the ball ")
        print("lives left:",config.lives,"   score:" , config.score+global_variables.explosion_score() , "     time till now:",int(global_variables.total_time))
        global_variables.powerup_top_string()
        for y in range( self.height):          
            lol = []
            for x in range( 0 , config.columns):
                lol.append(self.matrix[y][x] + Style.RESET_ALL)
            
            print(''.join(lol))

    def border(self):
        for x in range(self.length):
            self.matrix[3][x] = "X"

        for x in range(self.length):
            self.matrix[39][x] = "="
        
