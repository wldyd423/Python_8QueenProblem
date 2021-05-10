#States: Any arrangement of 0 to 8 queens on the board is a state
#Initial state: No queens on the board.
#Actions: add a queen to any empty square
#Transition model: Return the board with a queen added to the specified square
#Goal test: 8 queens are on the board, none attacked.

import Debugging
import PySimpleGUI as sg
import ChessboardGUI as cg
import io
from PIL import Image

BoardSize = 400

db = Debugging.SimpleDebuger()
db.DEBUG_ON = True


class SimpleSolution:
    def __init__(self):
        self.queen_position = [-1, -1, -1, -1, -1, -1, -1, -1]

    def check_attack(self):
        for i in range(8):
            for j in range(i + 1, 8):
                #db.simple_print(f"{i} {j}")
                if self.queen_position[i] == -1:
                    return True
                if self.queen_position[i] == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print(f"false between ({i}, {self.queen_position[i]}) and ({j}, {self.queen_position[j]})")
                    return False
                elif self.queen_position[i] + j - i == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print(f"false between ({i}, {self.queen_position[i]}) and ({j}, {self.queen_position[j]})")
                    return False
                elif self.queen_position[i] - j + i == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print(f"false between ({i}, {self.queen_position[i]}) and ({j}, {self.queen_position[j]})")
                    return False
        return True

    def force_set(self, arr):
        print(f"!Force set {arr}")
        if len(arr) == 8:
            self.queen_position = arr
        print(self.queen_position, arr)

    def append_queen(self, pos):
        for i in range(len(self.queen_position)):
            if self.queen_position[i] == -1:
                self.queen_position[i] = pos
                return True
        return False

    def goback(self):
        for i in range(len(self.queen_position)):
            if self.queen_position[i] == -1:
                self.queen_position[i-1] = -1
                return True
            elif i == len(self.queen_position):
                self.queen_position[i] = -1
                return True
        return False


d = SimpleSolution()
from random import choice

repetition_count = 0

placement = dict([])
ss = SimpleSolution()
queens_placed = 0
while queens_placed < 8:
    print(queens_placed)
    #arr = ss.queen_position
    #print(f"Array setup {arr}")
    try:
        placement[queens_placed] = choice([i for i in range(0, 8) if i not in placement.values()])
    except:
        print("Break by exception")
        break
    ss.append_queen(placement[queens_placed])

    if not ss.check_attack():
        print("Found attack")
        print(placement)
        queens_placed -= 1
        ss.goback()
        #ss.force_set(arr)
        repetition_count += 1
        if repetition_count > 5:
            print("break by repetition")
            break
    else:
        repetition_count = 0
    queens_placed += 1



print(ss.queen_position)




img = Image.open('queen2.png')
img.thumbnail((BoardSize / 8, BoardSize / 8))
bio = io.BytesIO()
img.save(bio, format("PNG"))

k = cg.ChessboardGUI(BoardSize, bio.getvalue())

for key in placement:
    k.place_queen((key, placement[key]), k.graph)

while 1:
    event, value = k.window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

k.window.close()
