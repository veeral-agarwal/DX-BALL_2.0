from input import *
import os 
from time import sleep, time      
import time
from global_variables import *
import global_variables

if __name__ == "__main__":
    obj1 = Get()
    global_variables.flag = 0
    while(1):
        clear_components()
        check_powerup_timer()
        val = input_to(obj1)
        if val != None:
            sleep(0.05)
        if val == 'q' or is_life_left() == False or is_time_left()==False:
            break
        elif val == 'x':    
            shoot()
        elif val == 'a':
            move_left()
        elif val == 'd':
            move_right()
        render_all_components()
    print_final_scores()