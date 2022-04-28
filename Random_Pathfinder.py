import random

Board = [
         ['X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
         ['X', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
         ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
         ]
current_x = 0
current_y = 0
index_List = [(0, 0)]
count = 0

def set_path(List):
    for position in List:
        Board[position[0]][position[1]] = "#"
    print_board()
def print_board():
    for line in Board:
        for char in line:
            if char == "O":
               print("\033[1;36;40m" + char, end=" ")
            if char == "X":
                print("\033[1;31;40m" + char, end=" ")
            if char == "#":
                print("\033[1;32;40m" + char, end=" ")
        print()
while True:
    # sets direction list
    direction_list = ["up", "down", "left", "right"]
    
    # checks for edge case movement
    if current_x == 0:
        direction_list.remove("left")
    if current_x == len(Board[0]) - 1:
        direction_list.remove("right")
    if current_y == 0:
        direction_list.remove("up")
    if current_y == len(Board) - 1:
        direction_list.remove("down")
    
    if "left" in direction_list:
        if Board[current_y][current_x-1] == "X" or (current_y, current_x-1) in index_List:
            direction_list.remove("left")
    if "right" in direction_list:
        if Board[current_y][current_x+1] == "X" or (current_y, current_x+1) in index_List:
            direction_list.remove("right")
    if "up" in direction_list:
        if Board[current_y-1][current_x] == "X" or (current_y-1, current_x) in index_List:
            direction_list.remove("up")
    if "down" in direction_list:
        if Board[current_y + 1][current_x] == "X" or (current_y+1, current_x) in index_List:
            direction_list.remove("down")

    if len(direction_list) == 0:
        index_List.clear()
        current_x = 0
        current_y = 0
        index_List.append((0, 0))
        continue
    direction = random.choice(direction_list)

    if direction == "left":
        current_x -= 1
    if direction == "right":
        current_x += 1
    if direction == "up":
        current_y -= 1
    if direction == "down":
        current_y += 1
    index_List.append((current_y, current_x))
    if (current_y, current_x) == (len(Board) - 1, len(Board[0]) - 1):
        set_path(index_List)
        break
    count += 1

