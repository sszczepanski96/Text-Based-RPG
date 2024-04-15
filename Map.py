DESCRIPTION = 'description'
ENTERED = False
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
ITEM = 'item'
ENEMY = 'enemy'
SCREEN_WIDTH = 100

ITEMS = ['5 Gold', '10 Gold', '25 Gold', '50 Gold', '100 Gold', 'a Goblet', 'a Patch of Fur',
         'a Divine Scroll', 'a Flask', '135 Gold', '500 Silver', '40 Gold', 'a Mirrior',
         '152 Gold', '1,040 Silver', 'an Amber Gemstone', '28 Gold', '2,000 Copper', 'a Scroll'
         '120 Gold', 'a Copper Chamber Pot', '1,200 Copper', '4,000 Copper', 'a White Pearl',
         'a Carnelian Gemstone', '240 Gold', '360 Silver', '150 Silver', '120 Gold', 'a Silver Plate',
         '20 Gold', '55 Gold', '160 Silver', '55 Gold', '105 Gold', '25 Platinum', '12,500 Silver',
         'a Chain Shirt', '700 Silver', 'an Arcane Scroll', '5 Platinum']

entered_rooms = {'Dungeon Entrance': False, '2': False, '3': False, '4': False,
                 '5': False, '6': False, '7': False, '8': False, '9': False,
                 '10': False, '11': False, '12': False, '13': False, '14': False,
                 '15': False, '16': False, '17': False, '18': False, '19': False,
                 '20': False, 'Dungeon Exit': False}

map = {'Dungeon Entrance':{
        DESCRIPTION: ('There\'s a worn looking chandelier hanging from the cieling. The candles '
                      'almost burnt down to nothing. There\'s a rack on one of the walls holding a '
                      'single jar. You also see a pair of dirty dice on the ground. You decide not '
                      'to pick them up. Someone might miss them.\n'),
        ENTERED: False,
        UP: '3',
        LEFT: '2',
        ITEM: [],
        ENEMY: []
        },

        '2':{
        DESCRIPTION: ('The floor is covered in mud. Silver utensils, spikes, and wood scraps litter '
                      'the ground. Someone left a stuffed beast. The beasts that inhabit this dungeon '
                      'must not appreciate it very much.\n'),
        ENTERED: False,
        RIGHT: 'Dungeon Entrance',
        ITEM: [],
        ENEMY: []
        },

        '3':{
        DESCRIPTION: 'An empty room. Nothing spectacular in here!\n',
        ENTERED: False,
        UP: '4',
        DOWN: 'Dungeon Entrance',
        ITEM: [],
        ENEMY: []
        },

        '4':{
        DESCRIPTION: ('There\'s a crunch on the ground when you step into the room. To your horror, '
                      'you notice you stepped on teeth. Absolutely disgusting. There\'s a torn tapestry '
                      'on the wall, depicting something you can\'t quite make out.\n'),
        ENTERED: False,
        UP: '7',
        DOWN: '3',
        LEFT: '5',
        ITEM: [],
        ENEMY: []
        },

        '5':{
        DESCRIPTION: ('You notice words scrawled on the wall in some language you can\'t understand. '
                      'Amongst the scrawled words, you also see an evil symbol and an altar along one '
                      'of the walls. Pretty spooky in here.\n'),
        ENTERED: False,
        LEFT: '4',
        RIGHT: '6',
        ITEM: [],
        ENEMY: []
        },

        '6':{
        DESCRIPTION: ('There\'s a mound of rubble in a corner and a firepit in the middle. Maybe '
                      'someone was here recently. They left their blanket.\n'),
        ENTERED: False,
        LEFT: '5',
        ITEM: [],
        ENEMY: []
        },

        '7':{
        DESCRIPTION: 'Another boring, empty room. You\'d think a dungeon would be full of interesting things\n',
        ENTERED: False,
        UP: '9',
        DOWN: '4',
        LEFT: '8',
        ITEM: [],
        ENEMY: []
        },

        '8':{
        DESCRIPTION: ('There\'s a creepy arch in the middle of the room. It seems to have a thin '
                      'veil covering it. Best to leave it alone. There are playing cards strewn in '
                      'front of the arch as if someone dropped them in a hurry.\n'),
        ENTERED: False,
        RIGHT: '7',
        ITEM: [],
        ENEMY: []
        },

        '9':{
        DESCRIPTION: ('You step in a small puddle. What an inconvenience. There is mold growing on all '
                      'of the walls. There must be more water in here than you can see. A torn tapestry '
                      'hangs on the wall depicting an angel in battle. Why would that be here?\n'),
        ENTERED: False,
        UP: '17',
        DOWN: '7',
        LEFT: '10',
        RIGHT: '13',
        ITEM: [],
        ENEMY: []
        },

        '10':{
        DESCRIPTION: ('What a mess of a room. Dishes and tools are scattered all over the floor. A '
                      'cleaver is tossed to one side. A small firepit is tipped over. Maybe an "argument" '
                      'took place here.\n'),
        ENTERED: False,
        LEFT: '11',
        RIGHT: '10',
        ITEM: [],
        ENEMY: []
        },

        '11':{
        DESCRIPTION: ('There\'s a cage in this room of the dungeon and what look like, could that '
                      'be..? The dead body of an adventurer. Poor soul. Hopefully you\'ll have better luck.\n'),
        ENTERED: False,
        UP: '12',
        RIGHT: '10',
        ITEM: [],
        ENEMY: []
        },

        '12':{
        DESCRIPTION: ('Scorch marks cover the wall, giving the room a very gloomy atmosphere. There\'s '
                      'a statue of a knight toppled over and broken as well. Not so fun.\n'),
        ENTERED: False,
        DOWN: '11',
        ITEM: [],
        ENEMY: []
        },

        '13':{
        DESCRIPTION: ('There is bloodstains all over the walls and floor. Something not so nice must have '
                      'happened in here. Amongst the bones ans scraps of cloth you see a broken hourglass '
                      'and a drum. How odd.\n'),
        ENTERED: False,
        LEFT: '9',
        RIGHT: '14',
        ITEM: [],
        ENEMY: []
        },

        '14':{
        DESCRIPTION: ('There are nonhumanoid bones on the floor. You hope they are enemy bones but can\'t '
                      'be too sure. There are worn books strewn along the floor. Most of them look to be '
                      'water damaged.\n'),
        ENTERED: False,
        UP: '16',
        LEFT: '13',
        RIGHT: '15',
        ITEM: [],
        ENEMY: []
        },

        '15':{
        DESCRIPTION: ('Torches are hung on the wall. Only one is till completely lit. Someone must have '
                      'been here revently. There is a shallow pit in the middle of the room. The pit in '
                      'full of spikes. Better be careful moving around in here.\n'),
        ENTERED: False,
        LEFT: '14',
        ITEM: [],
        ENEMY: []
        },

        '16':{
        DESCRIPTION: ('There is a shelf on one of the walls. A couple books have been placed on it, along '
                      'with a human skull. Better them than you.\n'),
        ENTERED: False,
        DOWN: '14',
        ITEM: [],
        ENEMY: []
        },

        '17':{
        DESCRIPTION: ('You here the dripping of water. It sounds like it is coming from every direction. Where '
                      'could the water be coming from? Mold and slime cover the room.\n'),
        ENTERED: False,
        UP: '18',
        DOWN: '9',
        ITEM: [],
        ENEMY: []
        },

        '18':{
        DESCRIPTION: 'This room is empty. How unfortunate. Nothing interesting to look at in here.\n',
        ENTERED: False,
        UP: '19',
        DOWN: '17',
        ITEM: [],
        ENEMY: []
        },

        '19':{
        DESCRIPTION: ('A weapons rack stands against one of the walls. Unfortunately no weapons are being '
                      'displayed there. I guess you\'ll have to make due with what you already have. There '
                      'is a small idol laying on the floor. Hopefully a fellow adventurer only forgot about it...\n'),
        ENTERED: False,
        UP: 'Dungeon Exit',
        DOWN: '18',
        RIGHT: '20',
        ITEM: [],
        ENEMY: []
        },

        '20':{
        DESCRIPTION: ('This room is full of cobwebs. Obviously no one has been in here in a while. There is '
                      'a bed in the corner and the corpse of a monster laying on it. The bed looked inviting '
                      'until you saw the decaying body of the beast.\n'),
        ENTERED: False,
        LEFT: '19',
        ITEM: [],
        ENEMY: []
        },

        'Dungeon Exit':{
        DESCRIPTION: ('Finally! The exit to the dungeon. There is a double doorway across from where you are '
                      'standing. Freedom and safety are through those doors.\n'),
        ENTERED: False,
        DOWN: '19',
        ITEM: [],
        ENEMY: []
        },
        }
