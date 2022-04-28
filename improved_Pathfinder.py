from copy import copy
import time
import curses
from curses import wrapper
board = [
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

path_arr = [[(0, 1)]]
path = []

def print_board():
    for line in board:
        for char in line:
            if char == "X":
               print("\033[1;31;40m" + char, end="  ")
            if char == "O":
               print("\033[1;36;40m" + char, end="  ")
            if char == "#":
               print("\033[1;32;40mO", end="  ")
        print()

def clean_board():
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == "#":
                board[y][x] = "O"

def Available_indexes(x, y):
    available = []

    if(x + 1 <= 8):
        if (board[y][x+1] != "X"):
           available.append((y, x+1))
    if(x - 1 >= 0):
        if board[y][x-1] != "X":
           available.append((y, x-1))
    if(y+1 <= 8):
        if board[y+1][x] != "X":
           available.append((y+1, x))
    if(y - 1 >= 0):
        if board[y-1][x] != "X":
           available.append((y-1, x))
    return available

def set_path(path, check):
    for index in path:
        board[index[0]][index[1]] = "#"
        print_board()
        print("-------------------------")
    if check == 1:
        clean_board()

check = 1

while True:
    for path1 in path_arr:

        length = len(path1)
        index = path1[length-1]
        y = index[0]
        x = index[1]
        directions = Available_indexes(x, y)

        for direction in directions:
            path = copy(path1)
            if direction not in path:
               path.append(direction)
               path_arr.append(path)
               set_path(path, 1)

        for path1 in path_arr:
            if (8, 7) in path1:
                set_path(path1, 0)
                check = 0
                break

        if check == 0:
            break

    break
