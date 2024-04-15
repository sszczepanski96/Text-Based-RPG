######## IMPORT FILES AND MODULES #########
from Functions import *
from Classes import *
from Map import *
import os

######## INTRODUCTION #########
os.system('clear')
speech1 = 'Welcome to this simple dungeon crawler!\n'
speech2 = 'We hope it\'s not too difficult or boring.\n'
speech3 = 'The goal, so far, is to get to the end without dying!\n'
speech4 = '. . . kind of like life . . .\n'
speech5 = 'More features will be available when time permits it.\n'
speech6 = 'Good luck! And thanks for playing!\n'
type_string(speech1)
time.sleep(0.2)
type_string(speech2)
time.sleep(0.2)
type_string(speech3)
time.sleep(0.2)
type_string(speech4)
time.sleep(0.5)
type_string(speech5)
time.sleep(0.2)
type_string(speech6)
time.sleep(1)

####### TITLE SCREEN ########
initial_hero = Character('Joe', 12, 12, [], 0)
data = {'player':initial_hero, 'enemies':ENEMIES, 'map':map, 'items': ITEMS}
title_screen(data)
