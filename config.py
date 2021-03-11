import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
from math import pi
import numpy as np 

columns = 100
rows = 40

paddle = [['T','T','T','T','T'], ['T','T','T','T','T'] ]
shrink_p = [['T','T','T'], ['T','T','T'] ]
expand_p = [['T','T','T','T','T','T'], ['T','T','T','T','T','T' ]]

lives = 5
score = 0

fast_ball = [['f']]
thru_ball = [['t']]
shrink_paddle = [['s']]
expand_paddle = [['e']]
paddle_grab = [['p']]

ball = [['*']]
ball2 = [['o']]
brick = [['#','#','#']]
exploding = [['|','E','|']]