import random

CELL = [(0,0),(0,1),(0,2),(0,3),(0,4),
        (1,0),(1,1),(1,2),(1,3),(1,4),
        (2,0),(2,1),(2,2),(2,3),(2,4),
        (3,0),(3,1),(3,2),(3,3),(3,4),
        (3,0),(3,1),(3,2),(3,3),(3,4)]

def get_location():
  monster = random.choice(CELL)
  door = random.choice(CELL)
  player = random.choice(CELL)

  if monster == door or monster == player or door == player:
    return def_location()

  return monster, door, player

        
def move_player(player, move):
  x,y = player
  if move == "DOWN":
    x += 1
  elif move == "UP":
    x -= 1
  elif move == "LEFT":
    y -= 1
  elif move == "RIGHT":
    y += 1
  return x,y

def get_moves(player):
  moves = ["LEFT","RIGHT","UP","DOWN"]
  if player[1] == 4:
    moves.remove("RIGHT")
  if player[1] == 0:
    moves.remove("LEFT")
  if player[0] == 0:
    moves.remove("UP")
  if player[0] == 4:
    moves.remove("DOWN")
  return moves

def draw_map(player):
  print(" _ _ _ _ _")
  tile = "|{}"
  
  for idx, cell in enumerate(CELL):
    if idx in [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23]:
      if cell == player:
        print(tile.format("X"), end = "")
      else:
        print(tile.format("_"), end = "")
    else:
      if cell == player:
        print(tile.format("X|"))
      else:
        print(tile.format("_|"))
        
        
################START GAME##############
        
monster, door, player = get_location()
print("Welcome to the Dungeon")    
while True:
  moves = get_moves(player)

  print("Your currently in room {}".format(player))
  print(draw_map(player))
  print("You can move {}".format(moves))
  print("Enter QUIT to leave game")
        
  move = input("> ").upper()
        
  if move == "QUIT":
    break
        
  if move in moves:
    player = move_player(player, move)
  else:
    print("walls are hard, stop running into them")
    continue
  if player == door:
    print("Congrats you found the door.You WIN!")
    break
  elif player == monster:
    print("Not so fast, looks like the monster got you, Hahaha LOSER!")
    break