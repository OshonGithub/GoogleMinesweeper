import time
import pyautogui
import find

cell_locations = find.get_cell_locations()
cell_size, board_size = find.get_board_info()


top_left_region = (cell_locations[0][0][0] - cell_size, cell_locations[0][0][1] - cell_size)
bottom_right_region = (cell_locations[board_size[1] - 1][board_size[0] - 1][0] + cell_size, cell_locations[board_size[1] - 1][board_size[0] - 1][1] + cell_size)

board_region = (*top_left_region, bottom_right_region[0] - top_left_region[0] ,  bottom_right_region[1] - top_left_region[1])
print(board_region)

# unexplored = -1
# flagged = -2
# empty = 0
# rest of numbers are obvious
board_state = [[-1 for _ in range(board_size[0])] for _ in range(board_size[1])]

print("sleep")
time.sleep(2)

tic = time.perf_counter()
ones = list(pyautogui.locateAllOnScreen("numbers/1.png", grayscale=True, confidence=0.9))
twos = list(pyautogui.locateAllOnScreen("numbers/2.png", grayscale=True, confidence=0.9))

print(time.perf_counter() - tic)
for i in twos:
    pyautogui.moveTo(i.left, i.top)
    time.sleep(0.1)
print(twos)
print(len(twos))

