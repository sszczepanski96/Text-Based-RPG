################################
######## IMPORT MODULES ########
import sys
import time
import random
import os
import collections
import pickle
from Classes import *
from Map import *
from sys import platform
from tkinter import *
from PIL import Image, ImageTk
######## END IMPORT MODULES ########
####################################


################################
######## MISC FUNCTIONS ########
def main_game_loop(enemies, hero, items):
    while hero.dead == False:
        ### Ask player what they want to do
        prompt(enemies, hero, items)
        ### Winning the game
        if hero.location == 'Dungeon Exit':
            end_speech = 'You survived the Dungeon! I knew you could do it. \nWould you like to play again?\n'
            type_string(end_speech)
            answer = input('> ').strip().lower()
            ### Makes sure player input is valid
            while answer not in ['no', 'yes']:
                print('Please input a valid response (yes/no)')
                answer = input('> ').strip().lower()
            if answer == 'yes':
                if platform == "win32" or platform == "win64":
                    os.system('cls')
                else:
                    os.system('clear')
                ### Putting player back to dungeon entrance
                hero.location = 'Dungeon Entrance'
                ### Reset whether or not player has entered room
                for room in map.keys():
                    map[room][ENTERED] = False
                main_game_loop(enemies, hero, items)
                return
            ### Quits program
            elif answer == 'no':
                data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
                save_game(data)
                exit()
    if hero.dead == True:
        end_speech = 'You died! Would you like to try again?'
        type_string(end_speech)
        answer = input('> ').strip().lower()
        hero.dead = False
        while answer not in ['no', 'yes']:
            print('Please input a valid response (yes/no)')
            answer = input('> ').strip().lower()
        if answer == 'yes':
            main_game_loop(enemies, hero, items)
            return
        elif answer == 'no':
            data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
            save_game(data)
            exit()

### Types out words at a certain speed
def type_string(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
######## END MISC FUNCTIONS ########
####################################


####################################
######## MONSTERS FUNCTIONS ########
### Creates random list of enemies
def random_enemies(size, enemies, hero):
    ENEMIES = []
    for i in range(0, len(enemies)):
        ### Makes sure enemies levels aren't too high for player
        if enemies[i].challenge < hero.LEVEL:
            ENEMIES.append(enemies[i])
    return [random.choice(ENEMIES) for i in range(size)]

### Chance enemy is in a room
def room_enemies(enemies, hero):
    roll = Die(100).roll()
    size = random.randint(1, hero.LEVEL)
    ### Places enemy(s) in room (75% chance of enemies)
    if roll >= 40:
        map[hero.location][ENEMY] = random_enemies(size, enemies, hero)
######## END MONSTER FUNCTIONS ########
#######################################


################################
######## ITEM FUNCTIONS ########
def room_item(hero, items):
    map[hero.location][ITEM] = random.choice(items)
######## END ITEM FUNCTIONS ########
####################################


##########################################
######## TITLE SCREEN, LOAD, SAVE ########
### Display title menu
def title_screen(data):
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    print(' ----------------------------------------------\n',
          '               Welcome to Dungeon             \n',
          '----------------------------------------------\n',
          '                  - Continue -                \n',
          '                  - New Game -                \n',
          '                  -   Help   -                \n',
          '                  -   Quit   -                \n')
    ### Links options to actual functions
    title_screen_selections(data)

### Functions for title screen options
def title_screen_selections(data):
    option = input('> ').strip().lower()
    ### Make sure player input is valid
    while option not in ['continue', 'new game', 'help', 'quit']:
        print('Please enter a valid command.')
        title_screen_selections(data)
    if option == 'continue':
        load_game()
    elif option == 'new game':
        initialize_game(data)
    elif option == 'help':
        help_menu(data)
    elif option == 'quit':
        ### Saves progress so player doesn't lose it
        save_game(data)
        sys.exit()

def load_game():
    with open('savefile.json', 'rb') as f:
        ### Only need to save player data and enemy data
        data = pickle.load(f)
        hero = data['player']
        ENEMIES = data['enemies']
        map = data['map']
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    speech1 = 'Welcome back, '
    speech2 = hero.name
    speech3 = '\n\nLet\'s get to dungeoneering!'
    type_string(speech1)
    type_string(speech2)
    time.sleep(0.2)
    type_string(speech3)
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    hero.dead = False
    main_game_loop(ENEMIES, hero, ITEMS)

def initialize_game(data):
    ### Gets player class
    hero = profession()
    time.sleep(1)
    ### Gets player race, cosmetic purposes only
    hero_race = race()
    hero_avatar = CharacterAvatar(hero_race)
    time.sleep(1)
    ### Prints description/backstory
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    desc = player_description(hero, hero_race)
    CharacterBio(desc)
    ### Initialize enemies and items
    enemies = data['enemies']
    items = data['items']
    time.sleep(1)
    ### Introduction
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    speech1 = 'Hello '
    speech2 = hero.name
    speech3 = '. It\'s nice to meet you!\n'
    speech4 = 'No time for formalities though.\n'
    speech5 = 'Let\'s start this dungeon adventure.'
    type_string(speech1)
    type_string(speech2)
    type_string(speech3)
    time.sleep(0.2)
    type_string(speech4)
    time.sleep(0.2)
    type_string(speech5)
    time.sleep(1)
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    main_game_loop(ENEMIES, hero, ITEMS)
    ### Saving new data
    data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
    with open('savefile.json', 'wb') as f:
        pickle.dump(data, f)

def help_menu(data):
    print(' ----------------------------------------------\n',
          '               Welcome to Dungeon             \n',
          '----------------------------------------------\n',
          '> Use directions up, down, left, right to move\n',
          '> Type your commsnds to do them\n',
          '> Use "stats" to see your current stats\n',
          '> Use "commands" for a list of commands\n',
          '> To win the game, get to the end of the dungeon\n',
          '\n > Press ENTER to return to the menu')
    answer = input('> ').strip().lower()
    if answer == '':
        title_screen(data)


def save_game(data):
    with open('savefile.json', 'wb') as f:
        hero = data['player']
        enemies = data['enemies']
        map = data['map']
        items = data['items']
        ### Only need to save player data and enemy data
        save_data = {'player': hero, 'enemies': enemies, 'map': map, 'items': items}
        pickle.dump(save_data, f)
######## END TITLE SCREEN, LOAD, SAVE ########
##############################################


###################################
######## CHARACTER CHOICES ########
### Getting player class
def profession():
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    class_choice = ('Choose your class:\n1. Barbarian\n2. Bard\n3. Cleric\n4. Druid\n'
                    '5. Fighter\n6. Monk\n7. Paladin\n8. Ranger\n9. Rogue\n10. Sorcerer\n'
                    '\nPlease input the number you wish to choose.\n')
    type_string(class_choice)
    pclass = input('> ').strip()

    ### Makes sure player input is valid
    while pclass not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('\nPlease input a valid option (1-10).\n')
        pclass = input('> ').strip()
    if pclass == '1':
        pclass = Barbarian()
    elif pclass == '2':
        pclass = Bard()
    elif pclass == '3':
        pclass = Cleric()
    elif pclass == '4':
        pclass = Druid()
    elif pclass == '5':
        pclass = Fighter()
    elif pclass == '6':
        pclass = Monk()
    elif pclass == '7':
        pclass = Paladin()
    elif pclass == '8':
        pclass = Ranger()
    elif pclass == '9':
        pclass = Rogue()
    elif pclass == '10':
        pclass = Sorcerer()
    return pclass

### Gets player race, cosmetic purposes only
def race():
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    race_choice = ('Choose your race:\n1. Dwarf\n2. Elf\n3. Halfling\n4. Human\n'
                   '5. Dragonborn\n6. Gnome\n7. Half-Elf\n8. Half-Orc\n9. Tiefling\n'
                   '10. Aasimar\n\nPlease input the number you wish to choose.\n')
    type_string(race_choice)
    prace = input('> ').strip()
    ### Make sure playe rinput is valid
    while prace not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('Please input a valid option (1-10).\n')
        prace = input('> ').strip()
    if prace == '1':
        prace = 'Dwarf'
    elif prace == '2':
        prace = 'Elf'
    elif prace == '3':
        prace = 'Halfling'
    elif prace == '4':
        prace = 'Human'
    elif prace == '5':
        prace = 'Dragonborn'
    elif prace == '6':
        prace = 'Gnome'
    elif prace == '7':
        prace = 'Half_Elf'
    elif prace == '8':
        prace = 'Half_Orc'
    elif prace == '9':
        prace = 'Tiefling'
    elif prace == '10':
        prace = 'Aasimar'
    return prace

### Gets player avatar, for cosmetic purposes only
#def CharacterAvatar(string):
#    avatar_selection_pic = Image.open('{}.png'.format(string))
#    avatar_selection_pic.show()
#    avatar_selection = input("Choose an avatar\n> ")
#    type(avatar_selection)
#    if avatar_selection == '1':
#        avatar = Image.open('{}1.png'.format(string))
#        avatar.show()
#    elif avatar_selection == '2':
#        avatar = Image.open('{}2.png'.format(string))
#        avatar.show()
#    elif avatar_selection == '3':
#        avatar = Image.open('{}3.png'.format(string))
#        avatar.show()
#    elif avatar_selection == '4':
#        avatar = Image.open('{}4.png'.format(string))
#        avatar.show()
#    return avatar
def change_img(canvas,image,file_ext,integer):
    canvas.delete("all")
    canvas.img = ImageTk.PhotoImage(file='{}{}.{}'.format(image,integer,file_ext))
    canvas.create_image(100,100, image=canvas.img)

def CharacterAvatar(string):
    #creation of Tkinter window
    window = Tk()
    window.geometry('400x400')
    window.title("Welcome to Dungeon! - An RPG")
    canvas = Canvas(window,width=399,height=399)
    canvas.pack()

    avatar_selection_pic = Image.open('{}.png'.format(string))
    tk_avatar_selection_pic = ImageTk.PhotoImage(avatar_selection_pic)
    canvas.create_image(200,200,image=tk_avatar_selection_pic)

    avatar_selection = input("Choose an avatar:\n> ")
    type(avatar_selection)
    change_img(canvas,string,'png',avatar_selection)

### Prints out player description/backstory
def player_description(hero, race):
    pclass = hero.PROF
    if pclass == 'Barbarian':
        if race == 'Dwarf':
            desc = ('You are a 45 year old hermit. You were born in a cave. Your mother abandoned you '
                    'and your father disappeared to an unknown fate. Your mother\'s parents raised you. '
                    'You lived in a small house and had few close friends. You had a very ordinary childhood. '
                    'You became a Barbarian because you were struck by lightning and lived. Afterwards, you '
                    'found a new strength within you that let you push beyond your limitations. There was a '
                    'terrible blight in your home town which caused crops to fails and many starved. You lost '
                    'the only mother you ever knew to the blight. You were wrongly accused of causing the blight, '
                    'the people of your home town didn\'t accept your Barbarian ways and looked for any excuse '
                    'to put you away. But now you\'re here, adventuring.')

        elif race == 'Elf':
            desc = ('You are a 25 year old criminal. You grew up poor with your single father. Your mother disappeared '
                    'one night taking  stroll in the woods. You have six siblings, three older and three younger. You '
                    'get along fairly well with all of your siblings. You grew up in a rundown shack. You always found it '
                    'easy to make friends and love being around people. You became a criminal because you\'ve always had a '
                    'problem with authority. No one helped you look for your mom when you knew something had happened to '
                    'her. A life of crime was the best way you could get back at those who abandonded you. Through your '
                    'criminal activities, you ended up making an enemy of a fellow adventurer. You try to keep your distance '
                    'from them.')

        elif race == 'Halfling':
            desc = ('You are a 15 year old sailor. You grew up poor with both of your parents. They could only afford '
                    'to feed one extra mouth and so you are an ony child. You lived in a small house, just big enough '
                    'for you, your mother and your father. You grew up with few companions, most saw you as strange. '
                    'You became a sailor because it was one of the fastest ways you could get out of your small community. '
                    'You stowed away on a ship and were caught by the crew. Instead of killing you for trespassing, they '
                    'forced you to work for your passage and there you have stayed. Becoming a Barbarian wasn\'t much of '
                    'a choice for you, it was destinty. You lost control in a battle one day and it was as as if something '
                    'was manipulating your body, forcing it to kill every foe you could reach.')

        elif race == 'Human':
            desc = ('You are a 47 year old charlatan. You grew up quite comfortably with your single mother. Your father '
                    'was long gone by the time you were born. You have one younger sibling, alive and well. You lived in a '
                    'mansion and spent most of your childhood alone, exploring the walls and corridors of your own home, '
                    'hoping one day to go on an adventure. Being left to your own devices allowed you to hone your skills '
                    'in manipulating others. You are naturally an angry person and so you thought becoming a Barbarian would '
                    'be the best fit. Your anger needed to be channeled into battle. You\'ve spent your time working odd jobs, '
                    'being hired as muscle, etc.')

        elif race == 'Dragonborn':
            desc = ('You are a 27 year old folk hero. You were born in a rubbish heap. You were raised by your single mother. '
                    'Your father was imprisoned for stealing bread. You have two younger siblings, neither of them evil. You '
                    'moved around a lot, your mother unable to keep a steady job. You have few close friends because of this. '
                    'Moving around a lot didn\'t allow for a decent environment for you to learn to control your anger. So you '
                    'decided that being a Barbarian would be the best path to channel your anger into something. The only parent '
                    'you ever knew died suddenly leaving you empty and more full of rage than ever.')

        elif race == 'Gnome':
            desc = ('You are a 54 year old criminal. You were born in the large house you grew up in. You were raised by your '
                    'single father who holds a high position among the nobles of your town. You have one older sibling that '
                    'grew up to be a successful academic, helped by the status of your family. You however, have a temper and '
                    'because of this had few close friends. You became a criminal because you hate authority, especially your '
                    'wealthy father and his friends. You take delight in knowing you\'ve become your father\'s worst nightmare. '
                    'One unfortunate day, a fight between you and another criminal got out of hand. It felt as if some other '
                    'force had control of your body and you killed everything and everyone within reach. How you choose to '
                    'handle this event is up to your future self.')

        elif race == 'Half_Elf':
            desc = 'Barbarian Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Barbarian Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Barbarian Tiefling description'

        elif race == 'Aasimar':
            desc = 'Barbarian Asimar description'

    elif pclass == 'Bard':
        if race == 'Dwarf':
            desc = 'Bard Dwarf description'

        elif race == 'Elf':
            desc = 'Bard Elf description'

        elif race == 'Halfling':
            desc = 'Bard Halfling description'

        elif race == 'Human':
            desc = 'Bard Human description'

        elif race == 'Dragonborn':
            desc = 'Bard Dragonborn description'

        elif race == 'Gnome':
            desc = 'Bard Gnome description'

        elif race == 'Half_Elf':
            desc = 'Bard Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Bard Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Bard Tiefling description'

        elif race == 'Aasimar':
            desc = 'Bard Asimar description'

    elif pclass == 'Cleric':
        if race == 'Dwarf':
            desc = 'Cleric Dwarf description'

        elif race == 'Elf':
            desc = 'Cleric Elf description'

        elif race == 'Halfling':
            desc = 'Cleric Halfling description'

        elif race == 'Human':
            desc = 'Cleric Human description'

        elif race == 'Dragonborn':
            desc = 'Cleric Dragonborn description'

        elif race == 'Gnome':
            desc = 'Cleric Gnome description'

        elif race == 'Half_Elf':
            desc = 'Cleric Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Cleric Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Cleric Tiefling description'

        elif race == 'Aasimar':
            desc = ('You are a 20 year old acolyte. You were born from a human mother and angelic father. You grew in and around '
                    'an old, sacred temple. You\'ve been told that your temple is the oldest surviving structure built to your '
                    'god. The priest in charge of your temple gave you a Sun pendant blessed by your god and you wear it always. '
                    'The pendant seems to carry the warmth and prescence of your god, comforting you in hard times. Sometimes when '
                    'things get dark, it is hard for you not to feel like a plaything of the gods and resent being alone. However, '
                    'you are dedicated to your cause and will not falter in your beliefs.')

    elif pclass == 'Druid':
        if race == 'Dwarf':
            desc = 'Druid Dwarf description'

        elif race == 'Elf':
            desc = 'Druid Elf description'

        elif race == 'Halfling':
            desc = 'Druid Halfling description'

        elif race == 'Human':
            desc = 'Druid Human description'

        elif race == 'Dragonborn':
            desc = 'Druid Dragonborn description'

        elif race == 'Gnome':
            desc = 'Druid Gnome description'

        elif race == 'Half_Elf':
            desc = ('You are a 26 year old noble. You grew up in an important family in your druid community. '
                    'You grew up in the forest to be closer to the natural magic of the world. You were mentored '
                    'by a nymph who you happened to come across while practicing your magic near a stream. The '
                    'Nymph taught you how to be one with nature and the importance of blending in and not leaving '
                    'your mark on nature. Your mentor gave you a vial of water from a sacred river and you keep it '
                    'with you wherever you go. The trees remind you of power and vitality, always seeming to grow '
                    'and thrive even when broken beyond repair. Your druid culture is very important to you.')

        elif race == 'Half_Orc':
            desc = 'Druid Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Druid Tiefling description'

        elif race == 'Aasimar':
            desc = 'Druid  Asimar description'

    elif pclass == 'Fighter':
        if race == 'Dwarf':
            desc = 'Fighter Dwarf description'

        elif race == 'Elf':
            desc = 'Fighter Elf description'

        elif race == 'Halfling':
            desc = 'Fighter Halfling description'

        elif race == 'Human':
            desc = 'Fighter Human description'

        elif race == 'Dragonborn':
            desc = 'Fighter Dragonborn description'

        elif race == 'Gnome':
            desc = 'Fighter Gnome description'

        elif race == 'Half_Elf':
            desc = 'Fighter Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Fighter Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Fighter Tiefling description'

        elif race == 'Aasimar':
            desc = 'Fighter Asimar description'

    elif pclass == 'Monk':
        if race == 'Dwarf':
            desc = 'Monk Dwarf description'

        elif race == 'Elf':
            desc = 'Monk Elf description'

        elif race == 'Halfling':
            desc = 'Monk Halfing description'

        elif race == 'Human':
            desc = 'Monk Human description'

        elif race == 'Dragonborn':
            desc = 'Monk Dragonborn description'

        elif race == 'Gnome':
            desc = 'Monk Gnome description'

        elif race == 'Half_Elf':
            desc = 'Monk Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Monk Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Monk Tiefling description'

        elif race == 'Aasimar':
            desc = 'Monk Asimar description'

    elif pclass == 'Paladin':
        if race == 'Dwarf':
            desc = 'Paladin Dwarf description'

        elif race == 'Elf':
            desc = 'Paladin Elf description'

        elif race == 'Halfling':
            desc = 'Paladin Halfing description'

        elif race == 'Human':
            desc = 'Paladin Human description'

        elif race == 'Dragonborn':
            desc = 'Paladin Dragonborn description'

        elif race == 'Gnome':
            desc = 'Paladin Gnome description'

        elif race == 'Half_Elf':
            desc = 'Paladin Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Paladin Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Paladin Tiefling description'

        elif race == 'Aasimar':
            desc = 'Paladin Asimar description'

    elif pclass == 'Ranger':
        if race == 'Dwarf':
            desc = 'Ranger Dwarf description'

        elif race == 'Elf':
            desc = 'Ranger Elf description'

        elif race == 'Halfling':
            desc = 'Ranger Halfling description'

        elif race == 'Human':
            desc = ('You are a 28 year old outlander. You grew up on a farm close to an ancient forest. To make a '
                    'living you moved to the city to better take care of your family. However, you hate the city. '
                    'You believe walls are for cowards and cities breed weakness. They isolate people from the '
                    'harshness of the wild. While out making a living for your family, a horde of Goblins attacked '
                    'your family\'s farm and slaughtered your entire family. Now you seek revenge and kill every '
                    ' Goblin you come across.')

        elif race == 'Dragonborn':
            desc = 'Ranger Dragonborn description'

        elif race == 'Gnome':
            desc = 'Ranger Gnome description'

        elif race == 'Half_Elf':
            desc = 'Ranger Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Ranger Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Ranger Tiefling description'

        elif race == 'Aasimar':
            desc = 'Ranger Asimar description'

    elif pclass == 'Rogue':
        if race == 'Dwarf':
            desc = 'Rogue Dwarf description'

        elif race == 'Elf':
            desc = 'Rogue Elf description'

        elif race == 'Halfling':
            desc = 'Rogue Halfing description'

        elif race == 'Human':
            desc = 'Rogue Human description'

        elif race == 'Dragonborn':
            desc = 'Rogue Dragonborn description'

        elif race == 'Gnome':
            desc = 'Rogue Gnome description'

        elif race == 'Half_Elf':
            desc = 'Rogue Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Rogue Half-Orc description'

        elif race == 'Tiefling':
            desc = 'Rogue Tiefling description'

        elif race == 'Aasimar':
            desc = 'Rogue Asimar description'

    elif pclass == 'Sorcerer':
        if race == 'Dwarf':
            desc = 'Sorcerer Dwarf description'

        elif race == 'Elf':
            desc = 'Sorcerer Elf description'

        elif race == 'Halfling':
            desc = 'Sorcerer Halfing description'

        elif race == 'Human':
            desc = 'Sorcerer Human description'

        elif race == 'Dragonborn':
            desc = 'Sorcerer Dragonborn description'

        elif race == 'Gnome':
            desc = 'Sorcerer Gnome description'

        elif race == 'Half_Elf':
            desc = 'Sorcerer Half-Elf description'

        elif race == 'Half_Orc':
            desc = 'Sorcerer Half-Orc description'

        elif race == 'Tiefling':
            desc = ('You are a 22 year old sage. You were born of a human and a devil. Unfortunately, people '
                    'fear you because of your background. Well except for a sinister cult which plans to exploit '
                    'your powers for their own benefit. Your immense power comes from your family bloodline and is '
                    'especially powerful because of your father\'s rank in the infernal realm. Your eyes tend to '
                    'glow when you get a devious idea, giving away your intentions whether you wanted to or not. '
                    'When you cast a spell, the area around you goes dark and gloomy, also adding to the fear that '
                    'people have towards you. For reasons unknown, you are always icy cold to the touch, probably '
                    'a reflection of your cold heart.')

        elif race == 'Aasimar':
            desc = 'Sorcerer Asimar description'
    return desc

def CharacterBio(biotext):
    bio = biotext
    root = Tk()
    root.geometry('300x300')
    root.title("Character Biography")
    bioWindowFrame = Frame(root).grid(column=0,row=0,ipadx=4,ipady=4,sticky=NSEW)
    Label(root,text="----------------",wraplength=300,justify=CENTER).grid(column=0,row=0,)
    Label(root,text="Your Biography",wraplength=300,justify=CENTER).grid(column=0,row=1,)
    Label(root,text="----------------",wraplength=300,justify=CENTER).grid(column=0,row=2,)
    Label(root,text=bio,wraplength=300,justify=LEFT).grid(column=0,row=3,)
######## END CHARACTER CHOICES ########
#######################################


##########################
######## LEVEL UP ########
def levelUp(hero):
    while hero.xp >= hero.LEVEL_2:
        hero.LEVEL +=1
        hero.MAX_HP += Die(hero.HD).roll()
        hero.hp = hero.MAX_HP
        if hero.PROF in ['Bard', 'Cleric', 'Druid', 'Sorcerer']:
            hero.MAX_MANA +=1
            hero.MANA = hero.MAX_MANA
        hero.LEVEL_2 = hero.LEVEL_2 * 2
######## LEVEL UP ########
##########################


################################
######## ACTION CHOICES ########
def player_move(enemies, hero, items):
    ### Getting which direction the player would like to go
    print('\nWhich direction would you like to go?')
    dest = input('> ').strip().lower()
    ### Makes sure the player can go that way
    if dest in ['up', 'down', 'left', 'right']:
        if dest in map[hero.location]:
            hero.location = map[hero.location][dest]
            ### Putting enemy(s) in room
            room_enemies(enemies, hero)
            ### Putting item in room
            room_item(hero, items)
            ### Printing stuff about the room
            print('\n', map[hero.location][DESCRIPTION])
            ### Seeing if the player has entered the room before
            if map[hero.location][ENTERED] == True:
                print('You have already entered this room. You must be going around in circles.')
            else:
                map[hero.location][ENTERED] = True
            ### Checks if there are enemies in the room
            if map[hero.location][ENEMY]:
                print('There are enemies in this room! You see:')
                ### Prints the name and how many of each enemy there are
                enemy_count = collections.Counter(map[hero.location][ENEMY])
                for enemy in enemy_count.keys():
                    print(enemy_count[enemy], '', enemy.name)
                print('\n')
            if map[hero.location][ENEMY]:
                print('Would you like to fight or flee? \nIf you would like to use your magic ',
                      '(assuming you have that ability) type "spell". You can also pick up any items')
                answer = input('> ').strip().lower()
                while answer not in ['fight', 'spell', 'flee', 'get']:
                    print('Choose a valid option please: fight, spell, flee')
                    answer = input('> ').strip().lower()
                if answer == 'flee':
                    ### Rolling for chance of successful flee
                    flee_roll = Die(100).roll()
                    if flee_roll >= 50:
                        print('You successfully fleed from the fight!\n')
                        prompt(enemies, hero, items)
                        ### Exits function
                        return
                    else:
                        print('Unfortunately you\'re unable to flee from this fight. Nice try.\n')
                        fight(map[hero.location][ENEMY], hero, items)
                elif answer == 'fight':
                    fight(map[hero.location][ENEMY], hero, items)
                    return
                elif answer == 'spell':
                    spell(map[hero.location][ENEMY], hero, items)
                    return
                elif answer == 'get':
                    get_item(map[hero.location][ENEMY], hero, items)
                    return
        else:
            print('You run into a wall. It might be dark but it\'s not that dark.\n',
                  'Watch where you\'re going next time. Choose a different direction.\n')
            ### Starting over, prompting the player to choose a direction
            player_move(enemies, hero, items)
    else:
        print('Please use the commands: up, down, left, right\n')
        player_move(enemies, hero, items)

def get_item(enemies, hero, items):
    item = input('\nWhich item would you like to pick up? ')
    ### Check if item in room and if specific item typed in room
    if 'item' in map[hero.location] and item in map[hero.location][ITEM]:
        ### Adds item to inventory
        hero.inventory += [item]
        print('\n', hero.inventory, '\n')
        ### Deletes item from room inventory
        map[hero.location][ITEM] = []
    else:
        print('There are no items for you to pick up here, try again.\n')
        ### Going back to initial prompt since there are no items to get
        prompt(enemies, hero, items)

def fight(enemies, hero, items):
    ### Fight each enemy seperately
    for enemy in enemies:
        ### Makes sure enemy is not dead
        while enemy.hp != 0:
            ### Rolls to see if enemy/player hits
            hero_roll = Die(20).roll()
            enemy_roll = Die(20).roll()
            ### Player hits enemy
            if hero_roll >= enemy.ac:
                ### Player gets a certain number of damage rolls depending on their level
                for i in range(0, hero.LEVEL):
                    ### Random amount of damage done based on Hit Die of player
                    hero_damage = Die(hero.HD).roll()
                    hero_damage += hero_damage
                ### Makes enemy HP go to zero instead of into negative numbers
                if hero_damage >= enemy.hp:
                    enemy.hp = 0
                ### Enemy HP goes down
                else:
                    enemy.hp -= hero_damage
                print('You hit the ', enemy.name, '!\n'
                      'The ', enemy.name, ' has ', enemy.hp, ' left.\n')
                time.sleep(0.5)
            else:
                print('You missed! You need more practice.\n',
                      'The ', enemy.name, ' has ', enemy.hp, ' health left.\n')
                time.sleep(0.5)
            ### Enemy hits
            if enemy_roll >= hero.ac:
                ### Automatically puts hero HP to zero if enemy does sufficient damage
                if enemy.damage >= hero.hp:
                    hero.hp = 0
                    print('Looks like you\'ve lost this battle. Maybe next time you\'ll ,'
                          'be able to get to the end of the dungeon\n',
                          'The ', enemy.name, ' did ', enemy.damage, ' damage instantly kill you.')
                    ### Putting hero back to dungeon entrance
                    hero.location = 'Dungeon Entrance'
                    ### Putting hero HP back to maximum
                    hero.hp = hero.MAX_HP
                    hero.dead = True
                    ### Resetting whether the player has entere the room
                    for room in map.keys():
                        map[room][ENTERED] = False
                    ### Better transition from dying to title menu
                    time.sleep(5)
                    ### Player can choose to quit or play again
                    data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
                    save_game(data)
                    title_screen(data)
                ### Player HP goes down
                else:
                    hero.hp -= enemy.damage
                    print('The ', enemy.name, 'hit you!\n',
                          'You have ', hero.hp, ' health left.\n')
            else:
                print('The ', enemy.name, ' missed. But the fight\'s not over yet.\n',
                      'You have ', hero.hp, ' health left.\n')
            ### Player HP sufficiently low, give the option to flee, if enemy still alive
            if hero.hp <= 5 and enemy.hp != 0:
                question = input('Would you like to try your luck and keep fighting or try to flee?\n> ').strip().lower()
                while question not in ['fight', 'flee']:
                    question = input('Please input a valid response: fight or flee\n> ').strip().lower()
                if question == 'flee':
                    ### Rolling for chance of successful flee
                    flee_roll = Die(100).roll()
                    if flee_roll >= 50:
                        print('You successfully fleed from the fight!\n')
                        prompt(ENEMIES, hero, items)
                        ### Exits function
                        return
                    else:
                        print('Unfortunately you\'re unable to flee from this fight. Nice try.\n')
                elif question == 'fight':
                    ### Continue fighting
                    continue
            ### Player gets experience points for defeating an enemy
            if enemy.hp == 0:
                print('The ', enemy.name, ' is dead!')
                hero.xp +=enemy.xp
            ### Small gap between fighting enemies
            time.sleep(1)
    # map[hero.location][ENEMY] = []
    time.sleep(2)
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')

def spell(enemies, hero, items):
    ### Makes sure player can use magic
    if hero.PROF in ['Bard', 'Cleric', 'Druid', 'Sorcerer']:
        ### Fighting enemies one at a time
        for enemy in enemies:
            ### Makes sure enemy isn't dead
            while enemy.hp != 0:
                ### Rolls to see if enemy/player hits
                hero_roll = Die(20).roll()
                enemy_roll = Die(20).roll()
                ### Player hits
                if hero_roll >= enemy.ac:
                    ### Player gets a certain amount of damage rolls depending on level
                    for i in range(0, hero.LEVEL):
                        hero_damage = Die(hero.HD).roll()
                        hero_damage += hero_damage
                    ### Making sure enemy HP doesn't go negative
                    if hero_damage >= enemy.hp:
                        enemy.hp = 0
                    ### Enemy HP goes down
                    else:
                        enemy.hp -= hero_damage
                    print('You hit the ', enemy.name, ' with your spell!\n'
                          'The ', enemy.name, ' has ', enemy.hp, ' left.\n')
                    ### Spells use up mana
                    hero.MANA -= 1
                else:
                    print('You missed! You need more practice, maybe a better instructor in the art of magic.\n',
                          'The ', enemy.name, ' has ', enemy.hp, ' health left.\n')
                ### Enemy hits
                if enemy_roll >= hero.ac:
                    ### Makes player HP zero if enemy does sufficient damage
                    if enemy.damage >= hero.hp:
                        hero.hp = 0
                        print('Looks like you\'ve lost this battle. Maybe next time you\'ll be able to get to the end of the dungeon')
                        ### Puts player back to Dungeon Entrance
                        hero.location = 'Dungeon Entrance'
                        ### Puts player HP back to maximum
                        hero.hp = hero.MAX_HP
                        hero.dead = True
                        ### Resetting whether the player has entered the room
                        for room in map.keys():
                            map[room][ENTERED] = False
                        ### Better transition from dying to title menu
                        time.sleep(5)
                        data = {'player': hero, 'enemies': enemies, 'map': map, 'items': ITEMS}
                        ### Player can choose to quit or play again
                        title_screen(data)
                    ### Player HP goes down
                    else:
                        hero.hp -= enemy.damage
                        print('The ', enemy.name, 'hit you!\n',
                              'You have ', hero.hp, ' health left.\n')
                else:
                    print('The ', enemy.name, ' missed. But the fight\'s not over yet.\n',
                          'You have ', hero.hp, ' health left.\n')
                ### When player runs out of mana, regular fighting is initiated
                if hero.MANA == 0:
                    print('You\'ve run out of mana. Time to use good old fighting techniques.\n')
                    ### Better transition between running out of mana and fighting
                    time.sleep(2)
                    fight(enemies, hero, items)
                    ### Exits function
                    return
                ### Time between hits
                time.sleep(1)
    else:
        print('Your character doesn\'t use magic. In your confusion you rush into the fight.\n')
        time.sleep(2)
        fight(enemies, hero, items)

def rest(enemies, hero):
    ### Makes sure there are no enemies in the room
    if map[hero.location][ENEMY]:
        print('You cannot rest while there are enemies nearby!\n')
    else:
        ### Puts player HP back to maximum
        if hero.hp < hero.MAX_HP:
            hero.hp = hero.MAX_HP
            print(hero.name, ' rests\n',
                  'Your current health is ', hero.hp, '\n')
        else:
            print('You rest but it doesn\'t seem to have done anything except waste time\n')
        ### Restores mana if player uses magic
        if hero.PROF in ['Bard', 'Cleric', 'Druid', 'Sorcerer']:
            if hero.MANA < hero.MAX_MANA:
                hero.MANA = hero.MAX_MANA
            else:
                print('Your mana is currently at its max.')

### Prints all important player attributes and their current values
def status(enemies, hero, items):
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    print('Your stats:\n',
          'NAME:        ', hero.name, '\n',
          'PROF:        ', hero.PROF, '\n',
          'LEVEL:       ', hero.LEVEL, '\n',
          'HEALTH:      ', hero.hp, '\n',
          'INVENTORY:   ', hero.inventory, '\n',
          'EXPERIENCE:  ', hero.xp)
    ### Prints current mana if player uses magic
    if hero.PROF in ['Bard', 'Cleric', 'Druid', 'Sorcerer']:
        print(' MANA:        ', hero.MANA, '\n')
    ### Calculating how much more experience points the player needs to level up
    xp_left = hero.LEVEL_2 - hero.xp
    print('Experience points needed for next level: ', xp_left, ' XP\n',
          '\nPress ENTER to return to game')
    answer = input('').strip().lower()
    if answer == '':
        if platform == "win32" or platform == "win64":
            os.system('cls')
        else:
            os.system('clear')
        ### If player pressed Enter, return to game
        prompt(enemies, hero, items)

### Prints out a list of commands that the player can type to do something
def commands(enemies, hero, items):
    if platform == "win32" or platform == "win64":
        os.system('cls')
    else:
        os.system('clear')
    print('----------------------------------------------\n',
          '                  Commands                    \n',
          '----------------------------------------------\n',
          '> "fight" to initiate fight\n',
          '> "flee" to flee from fight\n',
          '> "spell" to use magic (use magic before "fight")\n',
          '> "get" to pick up item\n',
          '> "rest" to regain HP and Mana\n',
          '> "status" to see current status of hero\n',
          '> "move" to initiate movement\n',
          '> "save" to save game\n',
          '> "quit" to exit to main menu\n',
          '\nPress ENTER to return to the game')
    answer = input('').strip().lower()
    if answer == '':
        ### If player pressed Enter, return to game
        if platform == "win32" or platform == "win64":
            os.system('cls')
        else:
            os.system('clear')
        prompt(enemies, hero, items)
######## END ACTION CHOICES ########
####################################


#############################
######## MAIN PROMPT ########
def prompt(enemies, hero, items):
    ### Seeing if the hero can level up
    levelUp(hero)
    ### Printing item in the room
    if map[hero.location][ITEM]:
        print('\nYou see', map[hero.location][ITEM], '\n')
    ### Getting what the player would like to do
    print('What would you like to do?')
    action = input('> ').strip().lower()
    ### Defining what actions the player is able to do
    acceptable_actions = ['move', 'quit', 'save', 'get', 'commands', 'status', 'rest']
    ### Keep getting player input until input is valid
    while action not in acceptable_actions:
        print('Unknown action, try again.')
        action = input('> ').strip().lower()
    if action == 'quit':
        ### Making sure the player actually wants to quit
        print('\nAre you sure you want to quit?')
        answer = input('> ').strip().lower()
        while answer not in ['no', 'yes']:
            print('\nPlease input a valid response (yes/no)')
            answer = input('> ').strip().lower()
        ### Continues game
        if answer == 'no':
            print('\nThat\'s what I thought. Keep on adventuring!')
            prompt(enemies, hero, items)
        elif answer == 'yes':
            data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
            title_screen(data)
            ### Exits function
            return
    elif action == 'save':
        data = {'player': hero, 'enemies': ENEMIES, 'map': map, 'items': ITEMS}
        save_game(data)
        print('Your game has been saved.\n')
    elif action == 'move':
        player_move(enemies, hero, items)
    elif action == 'get':
        get_item(enemies, hero, items)
    elif action == 'commands':
        commands(enemies, hero, items)
    elif action == 'status':
        status(enemies, hero, items)
    elif action == 'rest':
        enemies = map[hero.location][ENEMY]
        rest(enemies, hero)
######## MAIN PROMPT ########
#############################
