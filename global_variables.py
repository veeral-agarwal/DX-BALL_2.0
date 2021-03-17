from board import *
from objects import *
from config import *
import random
import numpy as np

b1=[]
b2=[]
stable_level2_bricks = [b1,b2]

level = 0
brick_falldown_flag = 0
exploding_bricks_flag = 0
level0starttime = 0
level1starttime = 0
level2starttime = 0

ball_privious_speed_y = 1
ball_privious_speed_x = 0

explosion_coordinates = []

main_board = Board()

main_paddle = Paddle(paddle , 5 , 35 ,lives)

main_ball = Ball(ball , 5 , 34)

main_ufo = UFO(ufo_design , 10,5)
main_bomb_1 = Bomb(bomb,global_variables.main_ufo.position_x , global_variables.main_ufo.position_y)

main_bullet = Bullet(bullet , global_variables.main_paddle.position_x , global_variables.main_paddle.position_y)

# main_bomb_2 = Bomb(bomb , global_variables.main_ufo.position_x+4 , global_variables.main_ufo.position_y)
# rainbow_b = Rainbow_bricks(brick , 10,9)

rainbow_brick_list = []
bricks_coor = []
bricks1 = []
bricks2 = []
bricks3 = [] 
bricks4 = []
bricks5 = []
exp_brick = []
bricks = [bricks1 , bricks2 , bricks3, bricks5 , bricks4 , exp_brick , rainbow_brick_list ]

def randomizer():
    if random.randint(1,4)==1: 
        return np.inf 
    
    else : 
        return random.randint(1,3)

for i in range(0 , 90 , 3):
    rainbow_brick_list.append(Rainbow_bricks(brick , i+5 , 5))
    bricks4.append(Brick(brick , i+5,6 ,randomizer() , 8 ))
    bricks1.append(Brick(brick , i+5,7 , randomizer() , 8 )) 
    bricks2.append(Brick(brick , i+5,11 , randomizer() , random.randint(7,7) ))
    bricks3.append(Brick(brick , i+5,9 , randomizer() , 8 ))
    if i >20 and i<45:
        exp_brick.append(Exploding_bricks(exploding , i+5 , 8)) 
    else:
        bricks5.append(Brick(brick ,i+5,8 , randomizer() , 8 ))
    bricks_coor.append((i+5 , 9))

def make_bricks():
    # if global_variables.level == 0:
    #     for i in range(0 , 90 , 3):
    #         bricks4.append(Brick(brick , i+5,5 ,randomizer() , 8 ))
    #         bricks1.append(Brick(brick , i+5,6 , randomizer() , 8 )) 
    #         bricks2.append(Brick(brick , i+5,10 , randomizer() , random.randint(6,6) ))
    #         bricks3.append(Brick(brick , i+5,8 , randomizer() , 8 ))
    #         if i >20 and i<45:
    #             exp_brick.append(Exploding_bricks(exploding , i+5 , 7)) 
    #         else:
    #             bricks5.append(Brick(brick ,i+5,7 , randomizer() , 8 ))
            # bricks_coor.append((i+5 , 9))
    if global_variables.level == 1:
        bricks_coor = []
        bricks1 = []
        bricks2 = []
        bricks3 = []
        bricks4 = []
        bricks5 = []
        exp_brick = []
        bricks = []
        rainbow_brick_list = []
        # bricks = [bricks1 , bricks2 , bricks3, bricks5 , bricks4 ,exp_brick ]

        for i in range(0 , 90 , 3):
            rainbow_brick_list.append(Rainbow_bricks(brick , i+5 , 12))
            bricks4.append(Brick(brick , i+5,5 ,randomizer() , 8 ))
            bricks1.append(Brick(brick , i+5,6 , randomizer() , 8 )) 
            bricks2.append(Brick(brick , i+5,10 , randomizer() , random.randint(7,7) ))
            bricks3.append(Brick(brick , i+5,8 , randomizer() , 8 ))
            if i >20 and i<45:
                exp_brick.append(Exploding_bricks(exploding , i+5 , 7)) 
            else:
                bricks5.append(Brick(brick ,i+5,7 , randomizer() , 8 ))
            bricks_coor.append((i+5 , 9))
        bricks = [bricks1 , bricks2 , bricks3, bricks5 , bricks4 ,exp_brick, rainbow_brick_list ]
        return bricks
    elif global_variables.level == 2:
        bricks_coor = []
        bricks1 = []
        bricks2 = []
        bricks3 = []
        bricks4 = []
        bricks5 = []
        exp_brick = []
        bricks = []
        rainbow_brick_list = []
        for i in range(0,90,10):
            bricks1.append(Brick(brick , i+5,7 , np.inf , 8 ))
        
        bricks = [bricks1 , bricks2 , bricks3, bricks5 , bricks4 ,exp_brick, rainbow_brick_list ]
        return bricks

fire_ball_list = []

flag = 0
powerupflag_thru_ball = 0
powerupflag_fast_ball = 0
powerupflag_expand_paddle = 0
powerupflag_shrink_paddle = 0
powerupflag_ball_multiplier = 0
powerupflag_paddle_grab = 0
powerupflag_fire_ball = 0
powerupflag_shooting_paddle = 0

active_powerupflag = [0,0,0,0,0,0,0,0]
inair_powerupflag = [0,0,0,0,0,0,0,0]

powerups = [powerupflag_ball_multiplier , powerupflag_expand_paddle , powerupflag_fast_ball , powerupflag_paddle_grab , powerupflag_shrink_paddle , powerupflag_thru_ball  
                                                                      ,powerupflag_fire_ball , powerupflag_shooting_paddle  ]
powerups_name = ["powerupflag_ball_multiplier" , "powerupflag_expand_paddle" , "powerupflag_fast_ball" , "powerupflag_paddle_grab" 
                            , "powerupflag_shrink_paddle" , "powerupflag_thru_ball" , "powerupflag_fire_ball" , "powerupflag_shooting_paddle" ]
powerup_start_time = [0,0,0,0,0,0,0,0]

powerup_objects = []

total_time = 0

def render_all_bricks():
    if global_variables.level == 0:
        for j in bricks:
            for i in j:
                i.clear()
                i.render()
                i.collision_ball_brick()
    else:
        for j in bricks:
            for i in j:
                i.clear()
                i.render()
                i.collision_ball_brick()
    for i in stable_level2_bricks:
        for j in i:
            j.clear()
            j.render()
            j.collision_ball_brick()
    

    
def powerup_top_string():
    active_powerups = []
    for i in range(len(active_powerupflag)):
        if active_powerupflag[i] == 1:
            active_powerups.append( powerups_name[i] )
    print("active powerups:")
    print(active_powerups)

def render_inair_powerup():
    for i in powerup_objects:
        i.clear()
        for j in range(8):
            if inair_powerupflag[j] == 1:
                i.clear()
                i.render()

def explosion_score():
    l1 = []
    cnt=0
    for i in explosion_coordinates:
        if i not in l1:
            cnt+=1
            l1.append(i)
    return cnt
    # print(cnt)

def shoot():
    if global_variables.flag == 0:
        main_ball.speed()
        global_variables.flag = 1

def move_left():
    if global_variables.flag == 0:
        main_ball.update_x_position(-2)

    main_paddle.update_x_position(-2)

def move_right():
    if global_variables.flag == 0:
        main_ball.update_x_position(2)
    
    main_paddle.update_x_position(2)

def render_all_components():
    render_all_bricks()
    main_ball.render()
    render_inair_powerup()
    main_paddle.render()
    main_board.render()
    if active_powerupflag[7] == 1:
        main_bullet.clear()
        main_bullet.render()
    else:
        main_bullet.shape = [[' ']]
        # print("lol")
    if global_variables.level == 2:
        main_ufo.clear()
        main_ufo.render()
        main_bomb_1.clear()
        main_bomb_1.render()
        # main_bomb_2.clear()
        # main_bomb_2.render()

def clear_components():
    main_paddle.clear()
    main_ball.clear()
    
    sys.stdout.write("\033c")
        
def check_powerup_timer():
    t = time.time()
    for i in range(len(active_powerupflag)):
        if t - powerup_start_time[i]>20:
            active_powerupflag[i] = 0

def print_final_scores():
    print("total time: ",global_variables.total_time)
    print("lives remaining: ",config.lives)
    print("score: ",config.score)

def is_time_left():
    if total_time>200:
        return False
    else:
        return True

def is_life_left():
    if config.lives>0:
        return True
    else:
        return False