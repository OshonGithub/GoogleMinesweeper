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


anc_loc = get_anchor_location()
pyautogui.moveTo(anc_loc.left, anc_loc.top)

def get_cell_locations():
    EASY_NUM, MED_NUM, HARD_NUM = 32, 111, 219 # the number of intersections for each difficulty
    cell_width, cell_height = -1, -1

    rtn_pos = []
    intersections = list(pyautogui.locateAllOnScreen("intersect.png"))

    mi_x, mx_x, mi_y, mx_y = -1, -1, -1, -1
    for i in intersections:
        mi_x = min(mi_x, i.left)
        mx_x = max(mx_x, i.left + i.width)

        mi_y = min(mi_y, i.top)
        mx_y = max(mx_y, i.top + i.height)

    intersections.append(2)
    if(len(intersections) == EASY_NUM):
        cell_width = (mx_x - mi_x) // 10
        cell_height = (mx_y - mi_y) // 8
    elif(len(intersections) == MED_NUM):
        cell_width = (mx_x - mi_x) // 18
        cell_height = (mx_y - mi_y) // 14
    elif(len(intersections) == HARD_NUM):
        cell_width = (mx_x - mi_x) // 24
        cell_height = (mx_y - mi_y) // 20
    else:
        print("Invalid number of intersects found!!!")
        return []



get_cell_locations()


