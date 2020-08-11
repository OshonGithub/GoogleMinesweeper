# find the location of the minesweeper game
import pyautogui
import time

def get_anchor_location():
    while True:
        anchor_location = pyautogui.locateOnScreen("anchor.png", grayscale=True, confidence=0.8)
        if(anchor_location == None):
            print("Cannot find game window... continuing search")
            continue
        return anchor_location

def get_cell_locations():
    EASY_NUM, MED_NUM, HARD_NUM = 32, 111, 219 # the number of intersections for each difficulty
    EASY_SIZE = (10, 8)
    MED_SIZE = (18, 14)
    HARD_SIZE = (24, 20)

    cell_size = -1
    board_size = (-1, -1)

    intersections = list(pyautogui.locateAllOnScreen("intersect.png"))

    mi_x, mx_x, mi_y, mx_y = 10**10, -1, 10**10, -1
    for i in intersections:
        mi_x = min(mi_x, i.left)
        mx_x = max(mx_x, i.left + i.width)

        mi_y = min(mi_y, i.top)
        mx_y = max(mx_y, i.top + i.height)

    if(len(intersections) == EASY_NUM):
        cell_size = 50
        board_size = EASY_SIZE
    elif(len(intersections) == MED_NUM):
        cell_size = 30
        board_size = MED_SIZE
    elif(len(intersections) == HARD_NUM):
        cell_Size = 15
        board_size = HARD_SIZE
    else:
        print("Invalid number of intersects found!!!")
        return []


    rtn_pos = [[] for _ in range(board_size[1])]
    for i in range(board_size[1]):
        for j in range(board_size[0]):
            rtn_pos[i].append((mi_x + (j*cell_size), mi_y + (i*cell_size)))

    return rtn_pos

cell_pos = get_cell_locations()


