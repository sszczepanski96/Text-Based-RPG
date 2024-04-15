import random
from Functions import *

def type_string(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

### GLOBAL VARIABLES
modifier = random.randint(0,5)
modifier2 = random.randint(0,2)

### CLASSES ###
### MAKING A DIE ###
class Die:
    # REPRESENTS A SINGLE DIE, DEFAULT TO 6 SIDES
    def __init__(self, sides=6):
        self.sides = sides
    # ROLLING THE DIE
    def roll(self):
        return random.randint(1, self.sides)
 ### END MAKING A DIE ###
class Character:
    def __init__(self, name, hp, ac, inventory, xp):
        self.name = name
        self.hp = hp
        self.ac = ac
        # INITIALIZE INVENTORY AS EMPTY
        self.inventory = []
        self.xp = xp

### PLAYER CLASSES ###
class Player(Character):
    def __init__(self, hp, ac, xp, location):
        self.location = location
        self.dead = False
        ask_name = '\nWhat do you call yourself?\n'
        type_string(ask_name)
        name = input('> ').strip()
        super().__init__(name, hp, ac, {}, xp)

class Barbarian(Player):
    HD = 12
    PROF = 'Barbarian'
    MAX_HP = 12 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 12 + modifier
        ask_ac = '\nChoose Light or Medium armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor']:
            print('Please input a valid response.')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'lightarmor']:
            ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'mediumarmor']:
            ac = 14 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')
        self.dead = False

class Bard(Player):
    HD = 8
    PROF = 'Bard'
    MANA = 1
    MAX_MANA = 1
    MAX_HP = 8 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 8 + modifier
        ac = 12 + modifier2
        super().__init__(hp, ac, 0, 'Dungeon Entrance')

class Cleric(Player):
    HD = 8
    PROF = 'Cleric'
    MANA = 1
    MAX_MANA = 1
    MAX_HP = 8 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 8 + modifier
        ask_ac = '\nChoose Light or Medium armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor']:
            print('Please input a valid response.')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'light armor']:
            ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'medium armor']:
            ac = 14 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')

class Druid(Player):
    HD = 8
    PROF = 'Druid'
    MANA = 1
    MAX_MANA = 1
    MAX_HP = 8 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 8 + modifier
        ask_ac = '\nChoose Light or Medium armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor']:
            print('Please input a valid response.')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'light armor']:
            ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'medium armor']:
            ac = 14 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')

class Fighter(Player):
    HD = 10
    PROF = 'Fighter'
    MAX_HP = 10 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 10 + modifier
        ask_ac = '\nChoose Light, Medium, or Heavy armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor', 'heavy', 'heavy armor']:
            print('Please input a valid response.')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'light armor']:
            ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'medium armor']:
            ac = 14 + random.randint(0,2)
        elif ac_choice in ['heavy', 'heavy armor']:
            ac = 16 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')

class Monk(Player):
    HD = 8
    PROF = 'Monk'
    MAX_HP = 8 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 8 + modifier
        ac = 10 + modifier2
        super().__init__(hp, ac, 0, 'Dungeon Entrance')

class Paladin(Player):
    HD = 10
    PROF = 'Paladin'
    MAX_HP = 10 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 10 + modifier
        ask_ac = '\nChoose Light or Medium armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor']:
            print('Please input a valid response.\n')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'light armor']:
                ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'medium armor']:
                ac = 14 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')


class Ranger(Player):
    HD = 10
    PROF = 'Ranger'
    MAX_HP = 10 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 10 + modifier
        ask_ac = '\nChoose Light or Medium armor\n'
        type_string(ask_ac)
        ac_choice = input('> ').strip().lower()
        if ac_choice not in ['light', 'light armor', 'medium', 'medium armor']:
            print('Please input a valid response.\n')
            ac_choice = input('> ')
        elif ac_choice in ['light', 'light armor']:
                ac = 12 + random.randint(0,2)
        elif ac_choice in ['medium', 'medium armor']:
                ac = 14 + random.randint(0,2)
        super().__init__(hp, ac, 0, 'Dungeon Entrance')


class Rogue(Player):
    HD = 8
    PROF = 'Rogue'
    MAX_HP = 8 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 8 + modifier
        ac = 12 + modifier2
        super().__init__(hp, ac, 0, 'Dungeon Entrance')


class Sorcerer(Player):
    HD = 6
    PROF = 'Sorcerer'
    MANA = 1
    MAX_MANA = 1
    MAX_HP = 6 + modifier
    LEVEL = 1
    LEVEL_2 = 300
    def __init__(self):
        hp = 6 + modifier
        ac = 10 + modifier2
        super().__init__(hp, ac, 0, 'Dungeon Entrance')
### END PLAYER CLASSES ###


### MONSTERS CLASSES###
class Monster(Character):
    def __init__(self, name, hp, ac, xp, challenge, damage):
        super().__init__(name, hp, ac, {}, xp)
        self.challenge = challenge
        self.damage = damage

class Bat(Monster):
    def __init__(self):
        DESC = 'Its a bat. Go look at a National Geographic book if you really don\'t know what a bat looks like.'
        super().__init__('bat', 1, 12, 10, 0, 1)

class Rat(Monster):
    def __init__(self):
        DESC = 'Its a rat. If you don\'t know what it looks like, count it as a blessing.'
        super().__init__('rat', 1, 10, 10, 0, 1)

class Spider(Monster):
    def __init__(self):
        DESC = 'Larger than your average spider but just as creepy. Better squash it before it does some real damage.'
        super().__init__('spider', 1, 12, 10, 0, 2)

class Kobold(Monster):
    def __init__(self):
        DESC = 'A small lizard-like creature. More humanoid than an actual lizard. Not exactly the friendly type though. Watch yourself!'
        super().__init__('kobold', 5, 12, 25, 1/8, 4)

class Stirge(Monster):
    def __init__(self):
        DESC = 'A small mosquito-like creature. More of a neuscence than anything else. But certaintly enough of a neuscence that it must be defeated.'
        super().__init__('stirge', 2, 14, 25, 1/8, 5)

class GiantRat(Monster):
    def __init__(self):
        DESC = 'Its a rat but much larger. So bigger teeth which would be more painful sinking into your flesh than a normal rat bite.'
        super().__init__('giant rat', 7, 12, 25, 1/8, 4)

class Goblin(Monster):
    def __init__(self):
        DESC = 'A small, gross looking creature. There is savagery in its eyes. It has long pointy ears, small, sharp teeth, and dirty looking green skin.'
        super().__init__('goblin', 7, 15, 50, 1/4, 5)

class Skeleton(Monster):
    def __init__(self):
        DESC = 'Not much to say other than its a skeleton that can move on its own and hurt you. So maybe don\'t try to make friends with it. Skeletons aren\'t supposed to move on their own.'
        super().__init__('skeleton', 13, 13, 50, 1/4, 5)

class Drow(Monster):
    def __init__(self):
        DESC = 'At first glance, you think you see an elf in the dark and you would be mostly correct. However, this elf is not your friend. This elf is selfish and cruel. Watch your back.'
        super().__init__('drow', 13, 15, 50, 1/4, 5)

class Hobgoblin(Monster):
    def __init__(self):
        DESC = 'Just like a goblin but larger and meaner. They are atuned to war and destruction. Which doesn\'t bode well for you. Watch out!'
        super().__init__('hobgoblin', 11, 18, 100, 1/2, 6)

class Magmin(Monster):
    def __init__(self):
        DESC = 'A small creature than look to be made of magma. Its body looks like cold, cracking lava witha fresh layer of lava underneath. It can hold flames in its hands and pierce you with its sharp claws.'
        super(). __init__('magmin', 9, 14, 100, 1/2, 7)

class Orc(Monster):
    def __init__(self):
        DESC = 'A slightly larger humanoid creature with two large tusks from the lower jaw. They are accustomed to war and destruction. Although not all of them are like this, this one in particular is not so nice, ready to attack.'
        super().__init__('orc', 15, 13, 100, 1/2, 9)

class Ghoul(Monster):
    def __init__(self):
        DESC = 'A humanoid creature with pale blue skin stands before you. You can feel its insatiable hunger for flesh. You back away before you can make out any more detailself.'
        super().__init__('ghoul', 22, 12, 200, 1, 9)

class Duergar(Monster):
    def __init__(self):
        DESC = 'At first it just looks like a dwarf that might be lost in the dungeon. But closer inspection reveals that its skin is a pale, pale purple. Its eyes are glazed over, almost white. You\'ve come to the conclusion you\'ve stumbled on an \'evil dwarf\'. Watch yourself.'
        super().__init__('duergar', 26, 16, 200, 1, 11)

class Imp(Monster):
    def __init__(self):
        DESC = 'A small demon-like creature. Its skin is red and has red, bat-like wings. You can tell this little creature is always up to no good.'
        super().__init__('imp', 10, 13, 200, 1, 10)

class DeathDog(Monster):
    def __init__(self):
        DESC = 'Its a dog, but worse, much much worse. A two-headed, evil looking, demon monstrocity. There is nothing cute anf fluffy about this dog.'
        super().__init__('death dog', 39, 12, 200, 1, 5)

class Ogre(Monster):
    def __init__(self):
        DESC = 'What is there to say? Its a large, distgusting looking creature. It smells like the old carion of its last meal. It is slow and dumb but quite strong. Don\'t turn your back on it! You may regret your choice.'
        super().__init__('ogre', 59, 11, 450, 2, 13)

class Basilisk(Monster):
    def __init__(self):
        DESC = 'A large serpent like creature with long, sharp fangs. You know from legend that you gazing into its eyes will turn you to stone'
        super().__init__('basilisk', 52, 15, 700, 3, 17)

class Manticore(Monster):
    def __init__(self):
        DESC = 'A very disturbing looking creature with the face of a man, the body of a lion the wings of a bat, and the sting of a scorpion. What kind of being would make such a disturbing mish-mash of a creature. Watch that stinger!'
        super().__init__('manticore', 68, 14, 700, 3, 7)

class Ettin(Monster):
    def __init__(self):
        DESC = 'A large, giant-like creature with two heads. Each head has two, large, sharp tusks coming from the lower jaw. Its a savage monster, grunting and stumbling around but not harmless, in fact its quite dangerous.'
        super().__init__('ettin', 85, 12, 1100, 4, 14)

class NightHag(Monster):
    def __init__(self):
        DESC = 'An wrinkly, old woman with dark blue skin. She has long, sharp nails and horns that come out of the top of the forehead. YOu know she\'s going to haunt your dreams for a long, long time.'
        super().__init__('night hag', 112, 17, 1800, 5, 13)

class Chimera(Monster):
    def __init__(self):
        DESC = 'With three heads: a lion\'s head, a goat\'s head, and a dragon\'s head, this creature is nothing like you\'ve ever seen. It has the claws of a lion in the front, the hooves of a goat in the back, and the wings and tail of a dragon. There are lots of things to watch out for.'
        super().__init__('chimera', 114, 14, 2300, 6, 11)

class Wyvern(Monster):
    def __init__(self):
        DESC = 'A smaller dragon-like creature, but certainly not small in size. Just SMALLER than an actual dragon. But just as dangerous.'
        super().__init__('wyvern', 110, 13, 2300, 6, 13)

class StoneGiant(Monster):
    def __init__(self):
        DESC = 'A large stone statue stands before you. With a closer looks you realize it\'s not a statue and is in fact alive and ready to fight.'
        super().__init__('stone giant', 126, 17, 2900, 7, 19)

class Fomorian(Monster):
    def __init__(self):
        DESC = 'A huge, giant-like creature. Very deformed, but quite muscular. Bumps and lumps cover most of its body. It carries a single club but you can tell it knows how to bludgeon its enemies.'
        super().__init__('fomorian', 149, 14, 3900, 8, 19)

class Hydra(Monster):
    def __init__(self):
        DESC = 'A large serpent like creatue with multiple heads. You\'ve learned from myth that you shouldn\'t try to cut off the heads, that\'ll just make everything worse, at least twice as many heads.'
        super().__init__('hydra', 172, 15, 3900, 8, 10)

class Beholder(Monster):
    def __init__(self):
        DESC = 'A large massive blob looking creature with one large eye that seems to gaze into your soul. There are tentacle like things squirming around its head that also have piercing eyes. Sharp teeth line the unnerving shape of its mouth. It must be quite dangerous.'
        super().__init__('beholder', 180, 18, 10000, 13, 17)

class BlackDragon(Monster):
    def __init__(self):
        DESC = 'A huge, black scaled dragon. Its belly is a gold color, beautifully contrasting the black of its other scales. Its wings are a little torn up, probably from battles well won. Unfortunately this dragon is not a friend. You should be careful.'
        super().__init__('black dragon', 195, 19, 11500, 14, 21)

class Demilich(Monster):
    def __init__(self):
        DESC = 'An immortal being that looks harmless but certainly isn\'t.As long as feeds on mortal souls it can stay alive forever. It\'s a floating skull with jewel like eyes. The glow of them makes you uneasy.'
        super().__init__('demilich', 80, 20, 20000, 18, 15)

class Balor(Monster):
    def __init__(self):
        DESC = 'A demon from the depths of hell. Its skin is a deep red and has large bat-like wings. It carries a whip of flame and a sword of lightning.'
        super().__init__('balor', 262, 19, 22000, 19, 21)
### END MONSTER CLASSES###

### INITIALIZING MONSTERS ###
bat = Bat()
rat = Rat()
spider = Spider()
kobold = Kobold()
stirge = Stirge()
giantRat = GiantRat()
goblin = Goblin()
skeleton = Skeleton()
drow = Drow()
hobgoblin = Hobgoblin()
magmin = Magmin()
orc = Orc()
ghoul = Ghoul()
duergar = Duergar()
imp = Imp()
deathDog = DeathDog()
ogre = Ogre()
basilisk = Basilisk()
manticore = Manticore()
ettin = Ettin()
nightHag = NightHag()
chimera = Chimera()
wyvern = Wyvern()
stoneGiant = StoneGiant()
fomorian = Fomorian()
hydra = Hydra()
beholder = Beholder()
blackDragon = BlackDragon()
demilich = Demilich()
balor = Balor()

ENEMIES = [bat, rat, spider, kobold, stirge, giantRat, goblin, skeleton, drow,
           hobgoblin, magmin, orc, ghoul, duergar, imp, deathDog, ogre, basilisk,
           manticore, ettin, nightHag, chimera, wyvern, stoneGiant, fomorian,
           hydra, beholder, blackDragon, demilich, balor]
### END INITIALIZING MONSTERS ###
