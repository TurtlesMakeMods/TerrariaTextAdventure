import random, sty
# Local Variables
# ---------------
# Overall map height
map_height = 20   
# This is the map itself
map = []          
# User's current X position
current_x = 0     
# User's current Y position
current_y = 0     
# Random 'edge of the world' messages
edge_messages = [
  'If you move that way, you will fall off the edge of the world...'  ,
  'You try, but you just can''t do it!',
  'Strange, you keep bouncing back to where you were.',
  'You *literally* hit a wall and bounce back'
]
# Random biome features
forest_features = [
  'in some trees',
  'in a wooded area',
  'under a tall pine',
  'under an unusually tall tree',
  'on top of an old stump',
  'near a cluster of cedars',
  'under the canopy of a great oak',
  'next to a huge hollowed out tree trunk'
]
desert_features = [
  'in a pile of sand',
  'near a cactus',
  'under a saguaro',
  'watching some javalina''s eat',
  'watching a lizard dance across the sand',
  'near a small sand dune'
]
corruption_features = [
  'knee deep in ooze',
  'on top of a smelly bog',
  'wishing you weren''t here'
]
ocean_features = [
  'near a school of fish',
  'surrounded by water',
  'in the shallow blue sea'
]
ice_features = [
  'on thin ice',
  'near a penguin',
  'knee deep in snow',
  'and sliding around'
]

# ---------------------------------------------------------------
# map_cell: One cell within a map will have various properties
# ---------------------------------------------------------------
class map_cell:
  def __init__(self, biome, feature, symbol, color, explored=False):
    self.biome = biome
    self.symbol = symbol
    self.explored = explored
    self.feature = feature
    self.color = color

# ---------------------------------------------------------------
# get_biome_feature: return a random feature based on the biome
# ---------------------------------------------------------------
def get_biome_feature(biome):
  if (biome == 'Forest'):
    return random.choice(forest_features)
  elif (biome == 'Desert'):
    return random.choice(desert_features)
  elif (biome == 'Corruption'):
    return random.choice(corruption_features)
  elif (biome == 'Ocean'):
    return random.choice(ocean_features)
  elif (biome == 'Ice'):
    return random.choice(ice_features)
  else:
    return ''
    
# ---------------------------------------------------------------
# add_biome: Add a biome to the end of the current map
# ---------------------------------------------------------------
def add_biome(biome, symbol, color, size):
  for x in range(size):
    new_col = []
    for y in range(map_height):
      new_col.append(map_cell(biome, get_biome_feature(biome), symbol, color))
    map.append(new_col)

# ---------------------------------------------------------------
# max_y: Maximum Y position on the map
# ---------------------------------------------------------------
def max_y():
  return len(map[0]) - 1

# ---------------------------------------------------------------
# max_x: Maximum X position on the map
# ---------------------------------------------------------------
def max_x():
  return len(map) - 1

# ---------------------------------------------------------------
# create_map: Create a new map
# ---------------------------------------------------------------
def create_map():
  global current_x, current_y
  
  # Add biomes
  add_biome('Ocean', 'O', sty.style.CBLUE, 5)
  add_biome('Forest', 'F', sty.style.CGREEN, 5)
  add_biome('Corruption', 'C', sty.style.CVIOLET2, 10)
  add_biome('Desert', 'D', sty.style.CYELLOW2, 10)
  add_biome('Forest', 'F', sty.style.CGREEN, 20)
  add_biome('Ice', 'I', sty.style.CBLUE2, 10)
  add_biome('Corruption', 'C', sty.style.CVIOLET2, 10)
  add_biome('Forest', 'F', sty.style.CGREEN, 5)
  add_biome('Ocean', 'O', sty.style.CBLUE, 5)

  # Set current position
  current_y = int(len(map[0]) / 2)
  current_x = int(len(map) / 2)
  map[current_x][current_y].explored = True
  
# ---------------------------------------------------------------
# show_full_map: Show the full map
# ---------------------------------------------------------------
def show_full_map():
  for y in range(max_y()+1):
    for x in range(max_x()+1):
      if current_x == x and current_y == y:
        print(f'{map[x][y].color}*{sty.style.CEND}', end='')
      else:
        if map[x][y].explored:
          print(f'{map[x][y].color}{map[x][y].symbol}{sty.style.CEND}', end='')
        else:
          print(f'{sty.style.CBLACK}\xb7{sty.style.CEND}', end='')
    print()

# ---------------------------------------------------------------
# show_small_map: Show a smaller map
# ---------------------------------------------------------------
def show_small_map():
  print('You are at x={}, y={}'.format(current_x, current_y))
  map_x = current_x - 2
  if (map_x < 0):
    map_x = 0
  map_y = current_y - 2
  if (map_y < 0):
    map_y = 0

  # Print the top line of the small map (+-+-+-+-+)
  for y in range(map_y, map_y+5):
    if (y <= max_y()):
      print('+-', end='')
  print('+')

  for y in range(map_y, map_y+5):
    if (y <= max_y()):
      for x in range(map_x, map_x+5):
        if (x <= max_x()):
          if current_x == x and current_y == y:
            print(f'|{map[x][y].color}*{sty.style.CEND}', end='')
          else:
            if (map[x][y].explored):
              print(f'|{map[x][y].color}{map[x][y].symbol}{sty.style.CEND}', end='')
            else:
              print('|\xb7', end='')
      print('|')

      # Print the dividing/bottom line of the small map (+-+-+-+-+)
      for y in range(map_y, map_y+5):
        if (y <= max_y()):
          print('+-', end='')
      print('+')

# ---------------------------------------------------------------
# move_up: move up one position in map
# ---------------------------------------------------------------
def move_up():
  global current_y 
  
  if (current_y == 0):
    print(random.choice(edge_messages))
  else:
    current_y = current_y - 1

# ---------------------------------------------------------------
# move_down: move down one position in map
# ---------------------------------------------------------------
def move_down():
  global current_y
  
  if (current_y == max_y()):
    print(random.choice(edge_messages))
  else:
    current_y = current_y + 1

# ---------------------------------------------------------------
# move_left: move left one position in map
# ---------------------------------------------------------------
def move_left():
  global current_x
  
  if (current_x == 0):
    print(random.choice(edge_messages))
  else:
    current_x = current_x - 1

# ---------------------------------------------------------------
# move_right: move right one position in map
# ---------------------------------------------------------------
def move_right():
  global current_x
  
  if (current_x == max_x()):
    print(random.choice(edge_messages))
  else:
    current_x = current_x + 1

# ---------------------------------------------------------------
# current_cell: return the current cell the user is in
# ---------------------------------------------------------------
def current_cell():
  return map[current_x][current_y]

# ---------------------------------------------------------------
# where_am_i: return a formatted message of where the user is
# ---------------------------------------------------------------
def where_am_i():
  print(f'You find youself standing {current_cell().feature} in a {current_cell().color}{current_cell().biome}{sty.style.CEND} biome')
    
# ---------------------------------------------------------------
# move: move a direction and print a nice message
# ---------------------------------------------------------------
def move(direction):
  direction = direction.strip().upper()
  if (direction == 'UP'):
    move_up()
  elif (direction == 'DOWN'):
    move_down()
  elif (direction == 'LEFT'):
    move_left()
  elif (direction == 'RIGHT'):
    move_right()
  else:
    print('Invalid direction')

  current_cell().explored = True

# ---------------------------------------------------------------
# map_help: show the map's help
# ---------------------------------------------------------------
def map_help():
  print('        -=> Map Help <=-')
  print('H or HELP               Help')
  print('U or MOVE UP            Move up')
  print('D or MOVE DOWN          Move down')
  print('L or MOVE LEFT          Move left')
  print('R or MOVE RIGHT         Move right')
  print('M or SHOW MAP           Show the full map')
  print('S or SHOW SMALL MAP     Show the small map')
  print('Q or QUIT               Quit the game')
  print()

  
# ---------------------------------------------------------------
# Main code
# ---------------------------------------------------------------
create_map()

# ---------------------------------------------------------------
# Code from main.py
# ---------------------------------------------------------------
"""

import map
while True:
  map.where_am_i()

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
"""
