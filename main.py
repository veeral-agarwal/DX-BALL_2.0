from input import *
import os 
from time import sleep, time      
import time
from global_variables import *
import global_variables
import objects

if __name__ == "__main__":
    
    lol = input("wanna sound [y/n]:")
    if lol == 'y':
        global_variables.wantsound = 1

    obj1 = Get()
    global_variables.flag = 0
    brickfalldownstarter = 0
    while(1):
        if brickfalldownstarter == 0:
            brickfalldownstarter = 1
            global_variables.level0starttime = time.time()
        clear_components()
        check_powerup_timer()
        val = input_to(obj1)
        if global_variables.brick_falldown_flag == 1:
            break

        if val != None:
            sleep(0.05)
        if val == 'q' or is_life_left() == False or is_time_left()==False or global_variables.main_ufo.lives<=0:
            break
        elif val == 'x':   
            shoot()
        elif val == 'a':
            move_left()
        elif val == 'd':
            move_right()
        elif val == 'l' or config.score == 180 or config.score == 360:
            if config.score == 180 or config.score == 360:    
                config.score+=1
            global_variables.level+=1
            if global_variables.level == 1:
                objects.levelskip()
                global_variables.level1starttime = time.time()
            elif global_variables.level == 2 :
                global_variables.level2starttime = time.time()
                objects.levelskip()
            else:
                break
        if global_variables.level==2 and int(global_variables.total_time)%5==0:
            if global_variables.wantsound == 1:
                os.system('aplay -q ./sounds/boss.mp3&')
            # pass
        render_all_components()
    print_final_scores()
    print(global_variables.level)
    if global_variables.main_ufo.lives<=0:
        print("you win")