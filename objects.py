import global_variables
import numpy as np
import config
from colorama import Fore, init , Back , Style
init()
import time
from time import time,sleep
import random
import math

class Objects():

    def __init__(self , obj , xpos , ypos):
        self.position_x = xpos
        self.position_y = ypos
        self.height = len(obj)
        self.width = len(obj[0])
        self.shape = obj

    def update_x_position(self , x):
        if self.position_x<=4:
            self.position_x=4
        
        if self.position_x>=90:
            self.position_x=90
        
        if self.position_x>1 and self.position_x<=90:
            self.position_x += x

    def update_y_position(self , y):
        self.position_y += y

    def current_position_x(self):
        return self.position_x

    def current_position_y(self):
        return self.position_y

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = " "

    def render(self):
        if global_variables.active_powerupflag[4] == 1 and global_variables.active_powerupflag[1] == 0:
            self.shape = config.shrink_p
            self.width = len(config.shrink_p[0])
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] =( Back.CYAN + Fore.CYAN + self.shape[j][i] )
        
        elif global_variables.active_powerupflag[1] == 1 and global_variables.active_powerupflag[4] == 0:
            self.shape = config.expand_p
            self.width = len(config.expand_p[0])
            # self.position_x -=1 
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] =( Back.CYAN + Fore.CYAN + self.shape[j][i] )

        elif (global_variables.active_powerupflag[1] == 1 and global_variables.active_powerupflag[4] == 1) or (global_variables.active_powerupflag[1] == 0 and global_variables.active_powerupflag[4] == 0):
            self.shape = config.paddle
            self.width = len(config.paddle[0])
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] =( Back.CYAN + Fore.CYAN + self.shape[j][i] )

class Paddle(Objects):

    def __init__(self ,obj , xpos , ypos, lives):
        self.initial_lives = 5
        self.score = 0
        super().__init__(obj , xpos , ypos)
        

    def lives(self):
        return self.initial_lives


class Ball(Objects):

    def __init__(self ,obj , xpos , ypos):
        super().__init__(obj , xpos , ypos)
        self.speed_x = 0
        self.speed_y = 0
        self.begin_time = time()
        self.onetimetempflag = 0

    def speed(self):
        self.speed_x = global_variables.ball_privious_speed_x
        self.speed_y = global_variables.ball_privious_speed_y

    def collision_with_wall(self):
        if self.position_x + self.speed_x<=1 or self.position_x+self.speed_x>=96:
            self.speed_x *= -1
        
        if self.position_y <=4:
            self.speed_y *= -1
        
        elif self.position_y + self.speed_y>=37:
            default()
            self.speed_x = 0
            self.speed_y = 0

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = " "

    def render(self):
        if global_variables.active_powerupflag[2] == 1 and self.onetimetempflag == 0:
            if self.speed_x < 0:
                self.speed_x -=1
            else:
                self.speed_x += 1
            self.onetimetempflag = 1

        self.collision_with_wall()
        self.collision_with_paddle()
        self.position_x += self.speed_x
        self.position_y -= self.speed_y
        
        for i in range(self.width):
            for j in range(self.height):
                global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = self.shape[j][i]

    def collision_with_paddle(self):
        if (global_variables.active_powerupflag[1] == 1 and global_variables.active_powerupflag[4] == 1) or (global_variables.active_powerupflag[1] == 0 and global_variables.active_powerupflag[4] == 0):
            if self.position_y == 35 or self.position_y == 36:
                if self.position_x == global_variables.main_paddle.position_x:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x -= 2
                
                elif self.position_x == global_variables.main_paddle.position_x+1:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else    :
                        self.speed_y *= -1
                        self.speed_x -= 1
                
                elif self.position_x == global_variables.main_paddle.position_x+2:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                
                elif self.position_x == global_variables.main_paddle.position_x+3:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else: 
                        self.speed_y *= -1
                        self.speed_x += 1
                
                elif self.position_x == global_variables.main_paddle.position_x+4:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x +=2

        elif global_variables.active_powerupflag[4] == 1 and global_variables.active_powerupflag[1] == 0:
            if self.position_y == 35 or self.position_y == 36:
                if self.position_x == global_variables.main_paddle.position_x:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x -= -1
                    
                elif self.position_x == global_variables.main_paddle.position_x+1:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                    # self.speed_x -= 1
                
                elif self.position_x == global_variables.main_paddle.position_x+2:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x += 1

        elif global_variables.active_powerupflag[1] == 1 and global_variables.active_powerupflag[4] == 0: 
            if self.position_y == 35 or self.position_y == 36:
                if self.position_x == global_variables.main_paddle.position_x:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x -= 2
                
                elif self.position_x == global_variables.main_paddle.position_x+1:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x -= 1
                
                elif self.position_x == global_variables.main_paddle.position_x+2:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                
                elif self.position_x == global_variables.main_paddle.position_x+3:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x += 1
                
                elif self.position_x == global_variables.main_paddle.position_x+4:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x +=2

                elif self.position_x == global_variables.main_paddle.position_x+4:
                    if global_variables.active_powerupflag[3] == 1:
                        global_variables.ball_privious_speed_x = self.speed_x
                        global_variables.ball_privious_speed_y = -1*self.speed_y
                        self.speed_y = 0
                        self.speed_x = 0
                        global_variables.flag = 0
                        global_variables.main_ball.position_y = 34
                    else:
                        self.speed_y *= -1
                        self.speed_x +=3

class Brick(Objects):

    def __init__(self, obj , xpos , ypos, weight , power ):
        super().__init__(obj , xpos , ypos)
        self.weight = weight
        self.score = 0
        self.flag = 0
        self.contain_powerup = power
        self.isexplosive = False

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if (self.weight > 0) and ((self.position_x,self.position_y) not in global_variables.explosion_coordinates):
                    if self.weight == 1:
                        global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ( Back.BLUE + Fore.BLUE + self.shape[j][i] )
                    
                    elif self.weight == 2:
                        global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ( Fore.GREEN + Back.GREEN  + self.shape[j][i])
                    
                    elif self.weight == 3:
                        global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ( Fore.RED +  Back.RED + self.shape[j][i] )
                    
                    elif self.weight == 4:
                        global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ( Fore.MAGENTA +  Back.MAGENTA + self.shape[j][i] )

                    elif self.weight == np.inf:
                        global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ( Fore.WHITE +  Back.WHITE + self.shape[j][i]  )
                
                else:
                    self.weight = 0
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] =' '
                    
    def collision_ball_brick(self):
        if self.isexplosive == False:
            if (self.position_x == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y) :
                if (self.weight > 0 and self.weight<4) or (self.weight == np.inf):
                    if global_variables.main_ball.speed_x != 0:
                        angle = math.degrees( math.atan(global_variables.main_ball.speed_y/global_variables.main_ball.speed_x) )
                        if ( angle>-45 and angle<45 ) : 
                            if global_variables.active_powerupflag[5] == 0:
                                global_variables.main_ball.speed_y *= -1
                        
                        else:
                            if global_variables.active_powerupflag[5] == 0:
                                global_variables.main_ball.speed_y *= -1
                    
                    else:
                        if global_variables.active_powerupflag[5] == 0:
                            global_variables.main_ball.speed_y *= -1
                
                if self.weight == 1:
                    config.score += 1  
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1 

                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1  

                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1  

                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1  
                
                global_variables.main_paddle.score += 1
                if global_variables.active_powerupflag[5] == 1:
                    self.weight = 0
                    config.score += 1   
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        # global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))
                
                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))

                else:
                    self.weight -= 1
            elif (self.position_x+1 == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y):
                if (self.weight > 0 and self.weight<4) or (self.weight == np.inf):
                    if global_variables.active_powerupflag[5] == 0:
                        global_variables.main_ball.speed_y *= -1

                if self.weight == 1:
                    config.score += 1   
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1 

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1
                
                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1
                    
                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1  

                global_variables.main_paddle.score += 1
                if global_variables.active_powerupflag[5] == 1:
                    self.weight = 0
                    config.score += 1   
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        # global_variables.inair_powerupflag[self.contain_powerup] = 1
                    
                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))
                    
                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))  

                else:
                    self.weight -= 1

            elif (self.position_x+2 == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y):
                if (self.weight > 0 and self.weight<4) or (self.weight == np.inf) :
                    if global_variables.main_ball.speed_x != 0:
                        angle = math.degrees( math.atan(global_variables.main_ball.speed_y/global_variables.main_ball.speed_x) )
                        if ((angle>135 and angle<=180)or(angle>=-180 and angle<-135)) : 
                            if global_variables.active_powerupflag[5] == 0:
                                global_variables.main_ball.speed_y *= -1
                
                        else:
                            if global_variables.active_powerupflag[5] == 0:
                                global_variables.main_ball.speed_y *= -1
                
                    else:
                        if global_variables.active_powerupflag[5] == 0:
                            global_variables.main_ball.speed_y *= -1
                
                if self.weight == 1:
                    config.score += 1  
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1 

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))
                        global_variables.inair_powerupflag[self.contain_powerup] = 1  

                global_variables.main_paddle.score += 1
                if global_variables.active_powerupflag[5] == 1:
                    self.weight = 0
                    config.score += 1   
                    if self.contain_powerup == 5:
                        global_variables.powerup_objects.append(Powerup(config.thru_ball , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 4:
                        global_variables.powerup_objects.append(Powerup(config.shrink_paddle , self.position_x , self.position_y , self.contain_powerup))
                        # global_variables.inair_powerupflag[self.contain_powerup] = 1

                    if self.contain_powerup == 1:
                        global_variables.powerup_objects.append(Powerup(config.expand_paddle , self.position_x , self.position_y , self.contain_powerup))
                    
                    if self.contain_powerup == 2:
                        global_variables.powerup_objects.append(Powerup(config.fast_ball , self.position_x , self.position_y , self.contain_powerup))

                    if self.contain_powerup == 3:
                        global_variables.powerup_objects.append(Powerup(config.paddle_grab , self.position_x , self.position_y , self.contain_powerup))

                else:
                    self.weight -= 1

class Exploding_bricks(Objects):
    def __init__(self , obj , xpos , ypos):
        super().__init__(obj , xpos , ypos)
        self.strength = 1
        self.isexplosive = True
        self.flag = 0

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = " "

    def render(self):
        if self.flag == 0:
            if ((self.position_x,self.position_y) in global_variables.explosion_coordinates):
                self.flag = 1
                self.strength = 0
                explosion_coor(self.position_x,self.position_y)
        for i in range(self.width):
            for j in range(self.height):
                if ((self.position_x,self.position_y) not in global_variables.explosion_coordinates):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = self.shape[j][i]
                else:
                    # explosion_coor(self.position_x,self.position_y)
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ' '

    def collision_ball_brick(self):
        if (self.position_x == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y) :
            explosion_coor(self.position_x,self.position_y)
            self.strength = 0
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ' '
        elif (self.position_x+1 == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y) :
            self.strength = 0
            explosion_coor(self.position_x,self.position_y)
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ' '
        elif (self.position_x+2 == global_variables.main_ball.position_x and self.position_y == global_variables.main_ball.position_y) :
            self.strength = 0
            explosion_coor(self.position_x,self.position_y)
            for i in range(self.width):
                for j in range(self.height):
                    global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = ' '

class Powerup(Objects):
    
    def __init__(self,obj,xpos,ypos , power):
        super().__init__(obj,xpos,ypos)
        self.speed_y = -1
        self.contain_powerup = power
        self.speed_flag = 0

    def render(self):
        if self.speed_flag == 0:
            # self.shape = [[' ']]
            self.position_y -= self.speed_y
        
        self.collision_with_paddle()
        for i in range(self.width):
            for j in range(self.height):
                global_variables.main_board.matrix[j+self.position_y][i+self.position_x] = (self.shape[j][i])
    
    def collision_with_paddle(self):
        # if (global_variables.active_powerupflag[1] == 1 and global_variables.active_powerupflag[4] == 1) or (global_variables.active_powerupflag[1] == 0 and global_variables.active_powerupflag[4] == 0):
        if self.position_y == 35 or self.position_y == 36:
            if self.position_x <= global_variables.main_paddle.position_x+global_variables.main_paddle.width and self.position_x >= global_variables.main_paddle.position_x:        
                self.speed_flag = 1
                # print(self.speed_y)
                self.position_y = 2
                global_variables.active_powerupflag[self.contain_powerup] = 1
                global_variables.powerup_start_time[self.contain_powerup] = time()
                global_variables.inair_powerupflag[self.contain_powerup] = 0
                self.shape = [[' ']]
        
        if self.position_y > 36:
            self.speed_y = 0
            self.speed_flag = 1

def explosion_coor(x,y):
    lol = []
    lol = [(x-3,y),(x+3,y),(x-3,y-1),(x+3,y-1),(x-3,y+1),(x+3,y+1),(x,y-1),(x,y+1),(x,y)]
    for i in lol:
        global_variables.explosion_coordinates.append(i)

def default():
    global_variables.main_paddle.clear()
    global_variables.main_ball.clear()
    config.lives -= 1
    global_variables.flag = 0
    global_variables.main_paddle.position_x=5
    global_variables.main_paddle.position_y=35
    global_variables.main_ball.position_x=5
    global_variables.main_ball.position_y=33

    #for fast ball
    global_variables.main_ball.onetimetempflag = 0
    
    global_variables.main_ball.render()
    global_variables.main_paddle.render()
    for i in range(len(global_variables.active_powerupflag)):
        global_variables.active_powerupflag[i] = 0