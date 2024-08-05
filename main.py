"""
This is Terraria Text Adventure! Originally made by
Titus Domey, Darius Collins, and Kiretan Amin, with assistance from Rafael Mather-Alvear.
T.T.A. is a "little" project we have been working on.
It is a text adventure style game similar to Zork, 
Planetfall, and other great I.F. games from the 80's, 
but strives to imitate the actual gameplay 
of the 2D indie survival game "Terraria".

TO DO LIST:
make rarity system for items - TITUS *almost done
incorporate inventory system - KIRETAN 
create separate inventory system for coins and ammo - KIRETAN *finished
weapon switch and equip system - KIRETAN 
crafting system - TITUS (btw i cant add until inventory is done but i will work on it in a diff repl)
"""
#hi

import threading, random, time, sys, map, sty

global source
# init local variables
toggle_help = 0
teoc_night = 0
player_health = 400
wait_duration = 1
nightValue = 0
skeletron = True

# music tracks
day = "OverworldDay.wav"
night = "OverworldNight.wav"
boss1 = "Boss1.wav"
boss2 = "Boss2.wav"
boss3 = "Boss3.wav"
roar = "Roar.wav"

# lists
old_man_dialogue_list = ["You are far too weak to defeat my curse.  Come back when you aren't so worthless.", "You pathetic fool.  You cannot hope to face my master as you are now.", "I hope you have like six friends standing around behind you.", "Please, no, stranger. You'll only get yourself killed.", "Stranger, do you possess the strength to defeat my master?", "You just might be strong enough to free me from my curse...", "Please! Battle my captor and free me! I beg you!", "Defeat my master, and I will grant you passage into the Dungeon.", "Try your luck, idiot. You won't get far."]
funny_fight_input_list = ["You got confused, and tried to pull out a stick! ", "You became very confused, and started to act like a chicken instead. ", "You suddenly have the urge to act just like a dog and roll in the dirt! ", "You become confused and try to fight with a plastic lightsaber in your backpack. "]
funny_begin_input_list = ["Your finger slipped and hit 'y' ", "You are going to play anyway. Sorry, not sorry. ", "Oooh, looks like your keyboard malfunctioned, time to play! "]
funny_scenario_input_list = ["You cant decide, so you try and fly like a bird instead. ", "You are indecisive, and start flopping on the ground like a fish. ", "You cant make up your mind, so you just stand there and stare at the clouds, hoping for inspiration. "]
Guide_Name_List = ["Andrew", "Asher", "Bradley", "Brandon","Brett","Brian","Cody","Cole", "Collin", "Connor", "Daniel", "Dylan", "Garrett", "Harley", "Jack", "Jacob", "Jake", "Jeff", "Jamal", "Jamaica", "Kyle", "Luke", "Ryan", "Steve", "Wyatt", "Chad", "Redigit"]
Ore_List = ["Copper Ore!","Iron Ore!", "Silver Ore!", "Platinum Ore!"]
inventory = []

# randomizing variables
old_man_dialogue = random.choice(old_man_dialogue_list)
Guide_Name = random.choice(Guide_Name_List)
sword_damage_value = random.randint(1,3)
bow_damage_value = random.randint(1,4)
monster_damage_value = random.randint(1,5)
explore_scene = random.randint(1,100)
scenario_value = random.randint(1,3)
mob_encounter = random.randint(1,2)
no = random.randint(0,0)

# ----------------------------------
# Classes
# ----------------------------------

class Item:
  def __init__(self, name):
    self.name = name
  def retName(self):
    return self.name

class Armor(Item):
  def __init__(self, name, defense, damage, crit, type):
    Item.__init__(self, name)
    self.defense = defense
    self.damage = damage
    self.crit = crit
    self.type = type
  def retClass(self):
    return self.type
  def retDef(self):
    return self.defense
  def retDam(self):
    return self.damage
  def retCrit(self):
    return self.crit
  
class Weapon(Item):
  def __init__(self, name, damage, crit, type, subclass):
    Item.__init__(self, name)
    self.damage = damage
    self.crit = crit
    self.type = type
  def retClass(self):
    return self.type
  def retSub(self):
    return self.subclass
  def retDam(self):
    return self.damage
  def retCrit(self):
    return self.crit
    
class Accessory(Item):
  def __init__(self, name, damage, crit, defense, dodge, type):
    Item.__init__(self, name)
    self.damage = damage
    self.crit = crit
    self.defense = defense
    self.dodge = dodge
    self.type = type
  def retClass(self):
    return self.type
  def retDam(self):
    return self.damage
  def retCrit(self):
    return self.crit
  def retDef(self):
    return self.defense
  def retDod(self):
    return self.dodge

class Ammo(Item):
  def __init__(self, name, damage, crit, debuff, type, pierce):
    Item.__init__(self, name)
    self.damage = damage
    self.crit = crit
    self.debuff = debuff
  def retDam(self):
    return self.damage
  def retCrit(self):
    return self.crit

class Buff:
  def __init__(self, name, damage, speed, defense, health, sight):
    self.damage = damage
    self.name = name
    self.speed = speed
    self.defense = defense
    self.health = health
    self.sight = sight

class Monster:
  def __init__(self, name, health, damage, defense, dodge, crit, debuff):
    self.name = name
    self.health = health
    self.damage = damage
    self.defense = defense
    self.dodge = dodge
    self.crit = crit
    self.debuff = debuff
  def retName(self):
    return self.name
  def retHea(self):
    return self.health
  def retDam(self):
    return self.damage
  def retDef(self):
    return self.defense
  def retDod(self):
    return self.dodge
  def retCrit(self):
    return self.crit
  def retBuff(self):
    return self.debuff

class Boss(Monster):
  def __init__(self, name, health, damage, defense, dodge, crit, debuff, theme):
    Monster.__init__(self, name, health, damage, defense, dodge, crit, debuff)

class Coin(Item):
  def __init__(self, name, value):
    Item.__init__(self, name)
    self.value = value
  def retValue(self):
    return self.value

# ----------------------------------
# Items, Buffs, and Armor
# ----------------------------------


#FOR RARITY - only add a color if it is not white, WHITE IS DEFAULT (for reference check fandom)
#example = Accessory("name", "damage", "crit", "defense", "dodge", "class")



solar = Armor("solar", 50, 30, 20, "melee")
trueNightEdge = Weapon(sty.style.CRED2 + "night's edge" + sty.style.CEND, 42, 42, "melee", 'other')
zenith = Weapon(sty.style.CRED2 + "zenith" + sty.style.CEND, 300, 20, "melee", 'other')
gauntlet = Accessory("gauntlet", 20, 10, 10, 10, "melee")
shackle = Accessory("shackle", 0, 0, 10, 2, "all")
ankhShield = Accessory("ankh shield", 10, 40, 0, 40, "ranger")
warriorEmblem = Accessory("warrior emblem", 30, 0, 0, 0, "melee")
rangerEmblem = Accessory("ranger emblem", 30, 0, 0, 0, "ranger")
noArmor = Armor("none", 0, 0, 0, "all")
noAcc = Accessory("none", 0, 0, 0, 0, "all")
noAmmo = Ammo("none", 0, 0, "none", "bullet", 0)
copperShortsword = Weapon("copper shortsword", 10, 0, "melee", "shortsword")
woodenBow = Weapon("wooden bow", 12, 0, "ranged", "bow") #the second number is extra crit chance, there is already innate crit of 10
musketBall = Ammo("musket ball", 8, 0, "none", "bullet", 1) #name, damage, crit, debuff, type, pierce(1 will mean it can hit one enemy before dissapearing)
silverBullet = Ammo("silver bullet", 10, 0, "none", "bullet", 1) #wait why pierce isnt our game turnbased meaning you fight one guy at once
woodenArrow = Ammo("wooden arrow", 6, 0, "none", "arrow", 1)
fire = Buff("on fire", 5, 0, 0, 0, "none")
noBuff = Buff("none", 0, 0, 0, 0, "none")
copperCoin = Coin("copper coin", 1)
silverCoin = Coin("silver coin", 100)
goldCoin = Coin("gold coin", 100000)
platinumCoin = Coin("platinum coin", 100000000)

# currently equipped
equip = { 
  "weapon": zenith,
  "armor": solar,
  "acc1": noAcc, 
  "acc2": noAcc,
  "acc3": noAcc,
  "acc4": noAcc,
  "acc5": noAcc,
  "ammoB": woodenArrow,
  "ammoG": musketBall
}
coins = {
  "c": 0,
  "s": 0,
  "g": 0,
  "p": 0
}

# ----------------------------------
# Functions
# ----------------------------------

# calculates coins
def combineCoins():
  while coins["c"] >= 100:
    coins["c"] = coins["c"]-100
    coins["s"] = coins["s"]+1
  while coins["s"] >= 100:
    coins["s"] = coins["s"]-100
    coins["g"] = coins["g"]+1
  while coins["g"] >= 100:
    coins["g"] = coins["g"]-100
    coins["p"] = coins["p"]+1
  if coins["p"] <= 0:
    coins["g"] += coins["p"]*100
    coins["p"] = 0
  if coins["g"] <= 0:
    coins["s"] += coins["g"]*100
    coins["g"] = 0
  if coins["s"] <= 0:
    coins["c"] += coins["s"]*100
    coins["s"] = 0
  if coins["c"] <= 0:
    coins["c"] = 0

# total coins
def totalCoins():
  return (coins["c"]*copperCoin.retValue()) + (coins["s"]*silverCoin.retValue()) + (coins["g"]*goldCoin.retValue()) + (coins["p"]*platinumCoin.retValue())

# displays amount of coins
def displayCoins():
  combineCoins()
  print("Copper coins: "+str(coins["c"]))
  print("Silver coins: "+str(coins["s"]))
  print("Gold coins: "+str(coins["g"]))
  print("Platinum coins: "+str(coins["p"]))

# for playing music in main thread
def play_audio(file):
  global source
  source = audio.play_file(file)
  source = source
  
#for playing music in background
def play_song(file):
  threading.Thread(args=(play_audio(file)))

# calculating defense for fights
def defense():
  d = equip["armor"].retDef() + equip["acc1"].retDef() + equip["acc2"].retDef() + equip["acc3"].retDef() + equip["acc4"].retDef()
  if equip["acc2"].retName() != equip["acc1"].retName():
    d -= equip["acc2"].retDef()
  if equip["acc3"].retName() != equip["acc2"].retName() and equip["acc3"].retName() != equip["acc1"].retName():
    d -= equip["acc3"].retDef()
  if equip["acc4"].retName() != equip["acc3"].retName() and equip["acc4"].retName() != equip["acc2"].retName() and equip["acc4"].retName() != equip["acc1"].retName():
    d -= equip["acc4"].retDef()
  if equip["acc5"].retName() != equip["acc4"].retName() and equip["acc5"].retName() != equip["acc3"].retName() and equip["acc5"].retName() != equip["acc2"].retName() and equip["acc5"].retName() != equip["acc1"].retName():
    d -= equip["acc5"].retDef()
  return d

# calculating damage for fights
def damage():
  d = equip["weapon"].retDam()
  d2 = 0
  if equip["weapon"].retClass() == equip["armor"].retClass() or equip["armor"].retClass() == "all":
    d2 += equip["armor"].retDam()/100
  if equip["weapon"].retClass() == equip["acc1"].retClass() or equip["acc1"].retClass() == "all":
    d2 += equip["acc1"].retDam()/100
  if (equip["weapon"].retClass() == equip["acc2"].retClass() or equip["acc2"].retClass() == "all") and equip["acc2"].retName() != equip["acc1"].retName():
    d2 += equip["acc2"].retDam()/100
  if (equip["weapon"].retClass() == equip["acc3"].retClass() or equip["acc3"].retClass() == "all") and equip["acc3"].retName() != equip["acc2"].retName() and equip["acc3"].retName() != equip["acc1"].retName():
    d2 += equip["acc3"].retDam()/100
  if (equip["weapon"].retClass() == equip["acc4"].retClass() or equip["acc4"].retClass() == "all") and equip["acc4"].retName() != equip["acc3"].retName() and equip["acc4"].retName() != equip["acc2"].retName() and equip["acc4"].retName() != equip["acc1"].retName():
    d2 += equip["acc4"].retDam()/100
  if (equip["weapon"].retClass() == equip["acc5"].retClass() or equip["acc5"].retClass() == "all") and equip["acc5"].retName() != equip["acc4"].retName() and equip["acc5"].retName() != equip["acc3"].retName() and equip["acc5"].retName() != equip["acc2"].retName()  and equip["acc5"].retName() != equip["acc1"].retName():
    d2 += equip["acc5"].retDam()/100
  d += d*d2
  if (equip["weapon"].retClass() == "ranged"):
    if equip["weapon"].retSub() == "gun":
      d += equip["ammoG"].retDam()
    elif equip["weapon"].retSub() == "bow":
      d += equip["ammoB"].retDam()
  return round(d)

# calculating crit values for fights
def crit():
  c = equip["armor"].retCrit() + equip["acc1"].retCrit() + equip["acc2"].retCrit() + equip["weapon"].retCrit() + equip["acc3"].retCrit() + equip["acc4"].retCrit() + equip["acc5"].retCrit() + 10
  if equip["acc2"].retName() != equip["acc1"].retName():
    c -= equip["acc2"].retCrit()
  if equip["acc3"].retName() != equip["acc2"].retName() and equip["acc3"].retName() != equip["acc1"].retName():
    c -= equip["acc3"].retCrit()
  if equip["acc4"].retName() != equip["acc3"].retName() and equip["acc4"].retName() != equip["acc2"].retName() and equip["acc4"].retName() != equip["acc1"].retName():
    c -= equip["acc4"].retCrit()
  if equip["acc5"].retName() != equip["acc4"].retName() and equip["acc5"].retName() != equip["acc3"].retName() and equip["acc5"].retName() != equip["acc2"].retName() and equip["acc5"].retName() != equip["acc1"].retName():
    c -= equip["acc5"].retCrit()
  if (equip["weapon"].retClass() == "ranged"):
    if equip["weapon"].retSub() == "gun":
      c += equip["ammoG"].retCrit()
    elif equip["weapon"].retSub() == "bow":
      c += equip["ammoB"].retCrit()
  return c

# for calculating dodge in fights
def dodge():
  d = equip["acc1"].retDod() + equip["acc2"].retDod() + equip["acc3"].retDod() + equip["acc4"].retDod() + equip["acc5"].retDod()
  if equip["acc2"].retName() != equip["acc1"].retName():
    d -= equip["acc2"].retDod()
  if equip["acc3"].retName() != equip["acc2"].retName() and equip["acc3"].retName() != equip["acc1"].retName():
    d -= equip["acc3"].retDod()
  if equip["acc4"].retName() != equip["acc3"].retName() and equip["acc4"].retName() != equip["acc2"].retName() and equip["acc4"].retName() != equip["acc1"].retName():
    d -= equip["acc4"].retDod()
  if equip["acc5"].retName() != equip["acc4"].retName() and equip["acc5"].retName() != equip["acc3"].retName() and equip["acc5"].retName() != equip["acc2"].retName() and equip["acc5"].retName() != equip["acc1"].retName():
    d -= equip["acc5"].retDod()
  return d

# ----------------------------------
# Monsters and Bosses
# ----------------------------------

#name of monster variable = Monster("monster name", health, damage, defense, dodge, crit, buff type, song name)

#monsters
  
slime = Monster("Slime", 14, 6, 0, 0, 50, noBuff)
zombie = Monster("Zombie", 45, 14, 6, 2, 20, noBuff)
demon_eye = Monster("Demon Eye", 60, 20, 2, 4, 20, noBuff)

#bosses
eye_of_cthulhu = Boss(sty.style.CRED + sty.style.CITALIC + "Eye of Cthulhu" + sty.style.CEND, 2800, 15, 12, 65, 12, noBuff, boss1)
eater_of_worlds = Boss(sty.style.CRED + sty.style.CITALIC + "Eater of Worlds" + sty.style.CEND, 3600, 13, 4, 23, 45, noBuff, boss1)
skeletron = Boss(sty.style.CRED + sty.style.CITALIC + "Skeletron" + sty.style.CEND, 4400, 32, 0, 11, 27, noBuff, boss2)
queen_bee = Boss(sty.style.CRED + sty.style.CITALIC + "Queen Bee" + sty.style.CEND, 3400, 22, 8, 75, 30, noBuff, boss3)
wall_of_flesh = Boss(sty.style.CRED + sty.style.CITALIC + "Wall of Flesh" + sty.style.CEND, 7600, 0, 94, 0, 30, fire, boss1)
twins = Boss(sty.style.CRED + sty.style.CITALIC + "Twins" + sty.style.CEND, 43000, 40, 10, 65, 55, noBuff, boss1)
destroyer = Boss(sty.style.CRED + sty.style.CITALIC + "Destroyer" + sty.style.CEND, 80000, 55, 35, 15, 70, noBuff, boss2)
skeletron_prime = Boss(sty.style.CRED + sty.style.CITALIC + "Skeletron Prime" + sty.style.CEND, 28000, 47, 24, 50, 94, noBuff, boss3)
plantera = Boss(sty.style.CGREEN + sty.style.CITALIC + "Plantera" + sty.style.CEND, 30000, 62, 36, 36, 78, noBuff, boss1)

moonlord = Boss(sty.style.CVIOLET+sty.style.CITALIC+"Moon Lord"+sty.style.CEND, 9999999, 9999999, 99999999, 999999, 9999999, fire, boss3)

# -----------------------
# | Inventory functions |
# -----------------------

def inInv(item): # this to check if it is inside an if statement like: if inInv(string of item you are checking): code
  if item in inventory:
    return True
  else:
    return False

def removeItem(item): # this to remove
  if item in inventory:
    inventory.remove(item)
    return "y"
  else:
    print("this item is not in your inventory")

def addItem(item): # this to add
  if len(inventory) < 50:
    inventory.append(item)
  else:
    while True:
      answer = input("Inventory full... remove item to make room? Y/N \n").strip().upper()
      if answer == "Y":
        print(inventory)
        it = input("What item to remove?")
        if removeItem(it) == "y":
          inventory.append(item)
        break
      else:
        break

        
#--------------------------
#| Damage check functions |
#--------------------------
        
def check_monster_damage(damage, crit, dodge, name, defense):
  mD = random.randint(1, 100)
  health = 0
  if mD <= 20:
    health = damage/2 + random.randint(-round((damage/2)/5), round((damage/2)/5)) - defense
    time.sleep(wait_duration)
    if health < 1:
        health = 1
    print("Ouch! The "+name+" hit you for "+str(round(health))+" damage!")
  if 20 < mD <= 100-dodge:
    if random.randint(1, 100) > crit:
      health = damage + random.randint(-round(damage/5), round(damage/5)) - defense
      time.sleep(wait_duration)
      if health < 1:
        health = 1
      print("Ow! The "+name+" hit you for for "+str(round(health))+" damage!")
    else:
      time.sleep(wait_duration)
      health = damage*2 + random.randint(-round((damage*2)/5), round((damage*2)/5)) - defense
      time.sleep(wait_duration)
      if health < 1:
        health = 1
      print("Critical! The "+name+" hit you for "+str(round(health))+" damage.")
  elif 100-dodge < mD <= 100:
    time.sleep(wait_duration)
    print("Nice, the "+name+"'s attack missed.")
  return int(health)
  
def check_weapon_damage(dodge, mName, defense):
  global equip
  d = random.randint(1, 100)
  health = 0
  if d <= 20:
    health = damage()/2 + random.randint(-round((damage()/2)/5), round((damage()/2)/5))
    time.sleep(wait_duration)
    if health < 1:
        health = 1
    print("Your "+equip["weapon"].retName()+" hit the "+mName+" for "+str(round(health))+" damage!")
  elif 20 < d <= 100-dodge:
    if random.randint(1, 100) > crit():
      health = damage() + random.randint(-round(damage()/5), round(damage()/5))
      time.sleep(wait_duration)
      if health < 1:
        health = 1
      print("Nice! Your "+equip["weapon"].retName()+" hit the "+mName+" for "+str(round(health))+" damage!")
    else:
      time.sleep(wait_duration)
      health = damage()*2 + random.randint(-round((damage()*2)/5), round((damage()*2)/5))
      time.sleep(wait_duration)
      if health < 1:
        health = 1
      print("Critical! Your "+equip["weapon"].retName()+" hit the "+mName+" for "+str(round(health))+" damage.")
  elif 100-dodge < d <= 100:
      time.sleep(wait_duration)
      print("Aww, your "+equip["weapon"].retName()+" missed.")
  return int(health)

#-----------------------------------
#| Main fight system loop/function |
#-----------------------------------

def fight_system(monster):
  global player_health
  global funny_fight_input
  global wait_duration
  global mob_drop_int
  global mobDrop
  global mobDrop_int
  global source
  mD = monster.retDam()
  mH = monster.retHea()
  mDe = monster.retDef()
  mDo = monster.retDod()
  mC = monster.retCrit()
  mN = monster.retName()
  #check for boss type
  if monster == eye_of_cthulhu or monster == skeletron:
    global source
    play_song(roar)
    source.paused = True
    time.sleep(2)
    play_audio(roar)
    play_song(boss1)
  #elif monster == moonlord:
    #source.paused = True
    #time.sleep(2)
    #play_song(boss1)
  while (True):
    # Display player health
    print("Player's HP = ", end = '')
    print(player_health)
    time.sleep(wait_duration)
    # Display monster health
    print(mN + "'s HP = ", end = '')
    print(mH)
    time.sleep(wait_duration)
    # Player turn
    print("Your turn. ")
    action = input("What action would you like to take? (Dodge, Attack, Parry, Run)\n").upper().strip()
    if action == "ATTACK" or action == "A":
      takeDamage = int(check_weapon_damage(mDo, mN, mDe))
      if takeDamage < 0:
          takeDamage = 1
          print("You did minimal damage")
      mH -= takeDamage
      dodgeBonus = 0
      defenseBonus = 0
    elif action == "DODGE" or action == "D":
      dodgeBonus = 30
      defenseBonus = 0
    elif action == "PARRY" or action == "P":
      defenseBonus = damage()/2
      dodgeBonus = 0
    elif action == "RUN" or action == "R":
      print("You ran away from the "+ mN)
      break
    elif action == "END" or action == "E":
      sys.exit()
    else:
      print(random.choice(funny_fight_input_list))
      dodgeBonus = 0
      defenseBonus = 0
    time.sleep(wait_duration)
    if (mH > 0):
      time.sleep(wait_duration)
      print("Monster's turn!")
      takeDamage = check_monster_damage(mD, mC, dodge() + dodgeBonus, mN, defense()+defenseBonus)
      player_health -= takeDamage
      time.sleep(wait_duration)
    if player_health <= 0:
      time.sleep(wait_duration)
      print("Out of health, You Died!")
      sys.exit()
    if mH <= 0:
      time.sleep(wait_duration)
      print("You have defeated the monster.")
      time.sleep(wait_duration)
      mob_drop()
      break      

def mob_drop(): #why dont we revamp this
    global mob_drop_int
    mob_drop_int = random.randint(1,100)
    silver = random.randint(1,99)
    copper = random.randint(1,99)
    mobDropCoins = str(silver) + " Silver and " + str(copper) + " Copper"
    mobDropAcc = gauntlet
    mobDropWeapon = woodenBow
    time.sleep(wait_duration)  
    if mob_drop_int >= 1 and mob_drop_int <= 50:
      print("The " + "monster" + " dropped " + mobDropCoins + "!")
    elif mob_drop_int >= 51 and mob_drop_int <= 60:
      print("The " + "monster" + " dropped " + mobDropCoins + "!")
    elif mob_drop_int >= 61 and mob_drop_int <= 70:
      print("The " + "monster" + " dropped " + mobDropCoins + "!")
    elif mob_drop_int >= 71 and mob_drop_int <= 80:
      print("The " + "monster" + " dropped " + mobDropCoins + "!")
    elif mob_drop_int >= 81 and mob_drop_int <= 95:
      print("The monster dropped " + mobDropAcc + "!")
    elif mob_drop_int >= 96 and mob_drop_int <= 100:
      print("The monster dropped " + mobDropWeapon.retName() + "!")

# -------------------------------
# | Scenarios |
# -------------------------------

# going mining
def run_mine():
    global funny_scenario_input
    global Ore_List
    global mined_ore
    time.sleep(wait_duration)
    mined_ore = random.choice(Ore_List)
    mined_ore_quantity = str(random.randint(10,50))
    #addItem(mined_ore)
    time.sleep(wait_duration)
    print("You decide to go on a mining expedition")
    time.sleep(wait_duration)
    print("*mining noises*")#we can add the mining sfx
    time.sleep(wait_duration)
    print("Eventually you find some ore: "+mined_ore_quantity+" "+mined_ore)
    time.sleep(wait_duration)
    print("Next, we should head back to the surface.")
    time.sleep(wait_duration)
    ask_player()

#going exploring
def run_explore(no):
    print("You look around and explore your surroundings.")
    eS = random.randint(1,100)
    if eS <= 25:
        time.sleep(wait_duration)
        slime_fight()
    elif eS >= 26 and eS <= 30:
        time.sleep(wait_duration)
        print("You encounter a chest - with some loot! Score!")
        check_scenario(scenario_value)
    elif eS >= 31 and  eS <= 60:
        print("You find a desert to the west! Watch out for the Antlions...")
        time.sleep(wait_duration)
        print("While you explore the desert, you find a desert cave!")
        while True:
            desert_cave_choice = input("Would you like to explore the cave? or keep moving?\n").upper().strip()
            if desert_cave_choice == str("EXPLORE THE CAVE"):
                time.sleep(wait_duration)
                ask_player()
                break
            elif desert_cave_choice == str("KEEP MOVING"):
                time.sleep(wait_duration)
                ask_player()
                break
            else:
                print("Please type either 'Explore the cave' or 'Keep moving'. ")
    elif eS >= 61 and eS <= 75:
        print("You find a glow mushroom cave. You see some Pirhanas in a lake.")
        fight_system(slime)
        run_mine()
    elif eS >= 76 and eS <= 100:
        print("You find a snow biome. Some Eskimo Zombies are approaching.")
        fight_system(zombie)
        run_mine()

# dont worry about this, its never used
def slime_fight():
    while True:
        basic_slime = input("A slime comes upon you! Fight? or Run?\n").upper().strip()
        if (basic_slime == str("FIGHT")):
            time.sleep(wait_duration)
            fight_system(slime)
            run_mine()
            break
        elif(basic_slime == str("RUN") or basic_slime == str("R")):
            time.sleep(wait_duration)
            print("You run, and the guide slays it with a bow and A LOT of arrows. (He's not a very good shot...)")
            time.sleep(wait_duration)
            run_mine()
            break
        else:
            print("Please type either 'Fight' or 'Run'. ")

# runs nighttime - also might spawn some bosses
def run_night():
  global night
  global teoc_night
  global nightValue
  global source
  source.paused = True
  play_song(night)
  teoc_night = random.randint(1,100)
  if teoc_night <= 95:
      print("Night has fallen!")
  elif teoc_night >= 96:
    print(sty.style.green + sty.style.CITALIC + "You feel an evil presence watching you." + sty.style.CEND)
    time.sleep(1.5)
    print("...")#play eerie sound effect and music here
    time.sleep(2)#start boss music
    print(sty.style.CRED2 + sty.style.CITALIC + "Eye of Cthulhu has awoken!" + sty.style.CEND)
    fight_system(eye_of_cthulhu)
  time.sleep(wait_duration)
  nightValue += 1
  check_mob_encounter(mob_encounter)
  ask_dungeon()

# if you have survived enough nights, you are able to go to a dungeon
def ask_dungeon():
  global nightValue
  while True:
      if nightValue >= 3:
        askDungeon = input("Would you like to go to the dungeon? Y/N\n").upper().strip()
        if askDungeon == str("Y"):
          run_dungeon()
          break
        elif askDungeon == str("N"):
          print("Ok, maybe next time.")
          break
        else:
          print("Please type either 'Y' or 'N'")
      else:
        break

# the actual dungeon scenario
def run_dungeon():
  global old_man_dialogue
  global skeletron
  global explore_dungeon
  time.sleep(wait_duration)
  print("You see a looming brick structure in the distance")
  time.sleep(wait_duration)
  while True:
    old_man = input("You see an old man. Would you like to talk to him? Y/N\n").upper().strip()
    if old_man == str("Y"):
      time.sleep(wait_duration)
      print(sty.style.CYELLOW+ "Old Man - " + "'" + old_man_dialogue + "'" + sty.style.CEND)
      curse_old_man = input("Would you like to curse him? Y/N\n").upper().strip()
      while True:
        if curse_old_man == str("Y"):
          print(sty.style.CGREEN + sty.style.CITALIC + "You feel the air grow colder around you." + sty.style.CEND)
          time.sleep(2)
          print("...") #eerie sound fx
          time.sleep(3)
          source.paused = True
          print(sty.style.CRED2 + sty.style.CITALIC + "Skeletron has awoken!" + sty.style.CEND)
          fight_system(skeletron)
          ask_player()
          break
        elif curse_old_man == str("N"):
          print("test")
          break
        else:
          print("Please type either 'Y' or 'N'\n")
    elif old_man == str("N"):
      print("You decide to not talk to the old man.")
      time.sleep(wait_duration)
      explore_dungeon = input("Would you like to go past him and explore the dungeon? Y/N\n").upper().strip()
      while True:
        if explore_dungeon == str("Y"):
          while True:
            if skeletron == False:
              time.sleep(wait_duration)
              print("You can't go here yet!")
              time.sleep(0.5)
              print(sty.style.CRED2 + "The dungeon gaurdians rip your body into shreds.\n" + sty.style.CEND)
              sys.exit()
            elif skeletron == True:
              time.sleep(wait_duration)
              print("skeletron")
              break
          else:
            print("Please type either 'Y' or 'N'\n")
        elif explore_dungeon == str("N"):
          print("Ok. Maybe go mining instead.\n")
          run_mine()
          break
        else:
          print("Please type either 'Y' or 'N'\n")
    else:
      print("Please type either 'Y' or 'N'\n")

# zombie encounter, also almost never used
def zombie_encounter():
    while True:
        zombie_fight = input("There is a Zombie! Fight or Run?\n").upper().strip()
        if (zombie_fight == str("FIGHT")):
            time.sleep(wait_duration)
            fight_system(zombie)
            ask_player()
            break
        elif (zombie_fight == str("RUN") or zombie_fight == str("R")):
            print("You try and run, but aren't fast enough and can't escape.")
            time.sleep(wait_duration)
            fight_system(zombie)
            ask_player()
            break
        else:
            print("Please type either 'Fight' or 'Run'. ")

#chop wood and build house scenarios
def run_chop_wood():
    print("Let's get some wood.")
    time.sleep(wait_duration)
    print("*wood chopping noises*")
    time.sleep(wait_duration)
    print("Nice! you've got some wood.")
    time.sleep(wait_duration)
    print("Now, you should build a house with that wood.")
    time.sleep(wait_duration)
    while True:
        HouseType = input("What kind of house? A or B?\n").upper().strip()
        if (HouseType == str("A")):
            print("You chose House type A, which has a rustic-modern look and is very suitable for NPCs")
            time.sleep(wait_duration)
            run_night()
            break
        elif(HouseType == str("B")):
            print("You chose House type B, which has a log-cabin look and is very suitable for NPCs")
            time.sleep(wait_duration)
            run_night()
            break
        else:
            print("Please type either 'A' or 'B'. ")

# gives a random scenario
def check_scenario(s):
    if s == 1:
        run_mine()
    elif s == 2:
        slime_fight()
    elif s == 3:
        run_explore(explore_scene)

#encountering a demon eye, never used lol
def demon_eye_encounter():
    while True:
        demon_eye_fight = input("There is a Demon Eye! Fight? or Run?\n").upper().strip()
        if (demon_eye_fight == str("FIGHT")):
            time.sleep(wait_duration)
            player_health = 150
            fight_system(demon_eye)
            ask_player()
            break
        elif (demon_eye_fight == str("RUN")):
            print("You try and run, but aren't fast enough and can't escape.")
            time.sleep(wait_duration)
            player_health = 150
            monster_health = 75
            fight_system(monster_health, player_health, 30, 0, 20, 10)
            ask_player()
            break
        else:
            print("Please type either 'Fight' or 'Run'. ")

# gives a random mob at night time
def check_mob_encounter(mob_type):
    if mob_type == 1:
        zombie_encounter()
    elif mob_type ==2:
        demon_eye_encounter()

# main function, asks what you want to do
def ask_player():
  global toggle_help
  while True:
    time.sleep(wait_duration)
    print("Your options are: ")
    print("  [1]Go Mining")
    print("  [2]Explore the world")
    print("  [3]Build")
    print("  [4]Pick for you")
    ask = input("What would you like to do?\n").upper().strip()
    #if ask == str("HELP"):
      
      #toggle_help = input("If you don't want these options to show up every time, type '1' if not type '0'\n").upper().strip()
     #if toggle_help == str("1"):
        #toggle_help == 1
        #break
      #elif toggle_help == str("0"):
        #print("ok, you won't see this anymore")
        #ask_player()
      #else:
        #print("That was not valid, try again")
        #ask_player()
    if ask == str("0"):
      print("Dev options: ")
      print("  [5]quit")
      print("  [6]run night")
      print("  [7]fight_system")
      print("  [8]check inventory")
      print("  [9]run dungeon")
      print("  [10]add coins")
      print("  [11]run map")
      print("  also all the regular options are available (:")
      ask = input("").upper().strip()
    if ask == str("1"):
      time.sleep(wait_duration)
      run_mine()
      break
    elif ask == str("2"):
      time.sleep(wait_duration)
      run_explore(no)
      break
    elif ask == str("3"):
      time.sleep(wait_duration)
      run_chop_wood()
      break
    elif ask == str("4"):
      time.sleep(wait_duration)
      check_scenario(scenario_value)
      break
    elif ask == str("5"):
      sys.exit()
      break
    elif ask == str("6"):
      run_night()
      break
    elif ask == str("7"):
      while True:
        dev_opt_fight = input("What mob do you want to test fight? (if you aren't sure type help)\n").upper().strip()
        if dev_opt_fight == str("SKELETRON"):
          fight_system(skeletron)
          ask_player()
          break
        elif dev_opt_fight == str("CTHULHU"):
          fight_system(eye_of_cthulhu)
          ask_player()
          break
        elif dev_opt_fight == str("EATER OF WORLDS"):
          fight_system(eater_of_worlds)
          ask_player()
          break
        elif dev_opt_fight == str("ZOMBIE"):
          fight_system(zombie)
          ask_player()
          break
        elif dev_opt_fight == str("SLIME"):
          fight_system(slime)
          ask_player()
          break
        elif dev_opt_fight == str("DEMON EYE"):
          fight_system(demon_eye)
          ask_player()
          break
        elif dev_opt_fight == str("MOONLORD") or dev_opt_fight == str("MOON LORD"):
          fight_system(moonlord)
          ask_player()
        elif dev_opt_fight == str("HELP"):
          print("Your options are: slime, cthulhu, skeletron, eater of worlds, zombie, demon eye, moonlord")
        else:
          print("Please enter a valid option")
    elif ask == str("8"):
      time.sleep(wait_duration)
      print(inventory)
    elif ask == str("9"):
      run_dungeon()
    elif ask == str("10"): 
      #mk just finish up and we gotta debug
      coins["c"] += int(input("How many copper coins to add/remove? "))
      coins["s"] += int(input("How many silver coins to add/remove? "))
      coins["g"] += int(input("How many gold coins to add/remove? "))
      coins["p"] += int(input("How many platinum coins to add/remove? "))
      print(coins)
      displayCoins()
    elif ask == str("11"):
      run_map()
    
    else:
      time.sleep(wait_duration)
      print("Please enter a valid command.")
def run_map():
  while True:
    map.where_am_i()
    print("Please fullscreen your console.")
    #time.sleep(2)
    print('What do you want to do?')
    c = input().strip().upper()
  
    if (c == 'HELP' or c == 'H'):
      map.map_help()
    elif (c == 'MOVE UP' or c == 'U'):
      map.move('UP')
    elif (c == 'MOVE DOWN' or c == 'D'):
      map.move('DOWN')
    elif (c == 'MOVE LEFT' or c == 'L'):
      map.move('LEFT')
    elif (c == 'MOVE RIGHT' or c == 'R'):
      map.move('RIGHT')
    elif (c == 'SHOW MAP' or c == 'M'):
      map.show_full_map()
    elif (c == 'SHOW SMALL MAP' or c == 'S'):
      map.show_small_map()
    elif (c == 'EXIT' or c == 'QUIT' or c == 'Q'):
      exit()
    else:
      print('Say wha???')
      map.map_help()

#colors :)



print("Please fullscreen your console, as it provides a much better playing experience.")
time.sleep(2)
print("Loading game...")
time.sleep(2)

while True:
    begin = input("Would you like to play? Y/N\n").upper().strip()
    if ((begin == str("Y")) or (begin == str(""))):
        time.sleep(0.1)
        while True:
            reader = input("Are you a slow, fast, or ULTRAFAST reader?\n").upper().strip()
            if (reader == str("SLOW")):
                wait_duration = 1
                break
            elif (reader == str("FAST")):
                wait_duration = 0.05
                break
            elif ((reader == str("ULTRAFAST")) or (reader == str(""))):
                wait_duration = 0
                break
            else:
                print("Please type either 'Slow', 'Fast', or 'Ultrafast'.")
        print("Great! Let's begin. ")
        time.sleep(wait_duration)
        #play_song(day)
        print("You enter the Overworld. ")
        time.sleep(wait_duration)
        print("You meet the guide, "+Guide_Name+".")
        if (Guide_Name == "Jamaica"):
            time.sleep(wait_duration)
            print("Welcome to Jamaica kid")
        time.sleep(wait_duration)
        ask_player()
        break
    elif (begin == str("N")):
        funny_begin_input = random.choice(funny_begin_input_list)
        print(funny_begin_input)
        time.sleep(wait_duration)
        ask_player()
        break
    elif (begin == str("QUIT")):
      sys.exit()
    elif (begin == str("ABSOLUTELY NOT")):
      print("My apologies. Good day to you, sir.")
      time.sleep(2)
      sys.exit()
    elif begin == str("EASTER EGG"):
      print("congrats. you found an easter egg.")
      print("thats it. what did you expect??")
      print(sty.style.CRED+"repl process died unexpectedly:"+sty.style.CEND)
      print(sty.style.CYELLOW+"›"+sty.style.CEND)
      time.sleep(200)
      print("why are you still here")
      print("I guess I'll have to give you an actual reward then.")
      time.sleep(2)
      print("...")
      time.sleep(3)
      print(sty.style.CGREEN+"impending doom approaches"+sty.style.CEND)
      time.sleep(5)
      fight_system(moonlord)
    else:
        print("Please type either 'Y' or 'N'. ")
