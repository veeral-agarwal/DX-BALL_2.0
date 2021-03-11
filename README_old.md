# DASS assignment - 2
# 2019114009

## explanation

an arcade game in Python3 (terminal-based), inspired from the old classic brick breaker similar to [this]()https://www.youtube.com/watch?v=BXEk0IHzHOM. The player will be using a paddle with a bouncing ball to smash a wall of bricks and make high scores! The objective of the game is to break all the bricks as fast as possible and beat the highest score! You lose a life when the ball touches the ground below the paddle.

Rules
-------------------

* you have 5 lives or 200 secs for game. 
* a life losses if you cross the lower boundary.
* you can take advantages of some powerups for 20 secs or some exploding bricks. 
* score increases by 1 if a brick exploded completely(different bricks have different strengths - 1,2,3,infinity and these are in different colours).

------------------------

Description of Classes 
--------------------------------------------
#### Board:
The board class creates a 40*100 board for gameplay, with all four boundaries. render function in this class is for printing our board(that 2-d matrix which we are updating).

#### Object:
The Object class is the parent class based on which some entities of the game are inherited (bricks , paddle , ball , exploding bricks , powerups).

#### Ball:
The Ball class has all the variables and functions of ball, this includes the shoot, movement, collisions. It is inherited from Object class and has additional functionality. It also represents polymorphism as the render() function has been changed.

#### Paddle:
The paddle class is inherited from the Object class and has function to move .

#### powerups:
The powerups class is inherited from Object class, it has function that check for collisions of powerups with paddle.

#### bricks:
The bricks class is inherited from Object class, it has function to check collisions of ball and bricks.

#### exploding bricks:
The exploding bricks class is inherited from Object class, it has function to check collisions of ball and bricks.
__________________

Concepts
--------------------------------------------

#### Inheritance:

Inheritance allows us to define a class that inherits all the methods and properties from another class. 
A base class `Object` has been declared from which multiple elements are inherited.

```python

class Objects():

    def __init__(self , obj , xpos , ypos):
        self.position_x = xpos
        self.position_y = ypos
        self.height = len(obj)
        self.width = len(obj[0])
        self.shape = obj

```

#### Polymorphism

Polymorphism allows us to define methods in the child class with the same name as defined in their parent class. 

```python
class Objects():
    ...
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
```
```python
class Ball(Objects):
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
```

#### Encapsulation

The idea of wrapping data and the methods that work on data within one unit. Prevents accidental modification of data.
Implemented many classes and objects for the same.

#### Abstraction

Abstraction means hiding the complexity and only showing the essential features of the object.

```python

class Ball(Objects):
    ...
    def speed(self):
        self.speed_x = global_variables.ball_privious_speed_x
        self.speed_y = global_variables.ball_privious_speed_y
```
.speed() is an abstraction

How To Play:
------------------

* Run the following code to start the game.
```
python3 main.py
```
* 'a,  d' use these controls for left, and right.
* use 'x' to shoot. 
* press 'q' to quit.

___________________

Reqiurements:
--------------------
- Python3

For mac:
```
brew cask update
sudo brew cask install python3
```
For Linux:
```
sudo apt-get update
sudo apt-get install python3
```
