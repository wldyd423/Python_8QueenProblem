##Extension of Simple Solution.
##Still uses incremental formulation
## Book does acknowledge the existance of superior method but that would be made later

import SimpleSolution
import PySimpleGUI as sg
import ChessboardGUI as cg
import io
from PIL import Image
from random import choice

class OpenSquareRegulator:
    def __init__(self):
        self.chessboard = [[0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7]]
    def reset(self):
        self.chessboard = [[0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7],
                           [0, 1, 2, 3, 4, 5, 6, 7]]
    def printboard(self):
        for i in range(8):
            print(self.chessboard[i])
    def place(self, coord):
        print("placeholder")
        #if given a coordinate at which a piece is place eliminate the attacking spots


#make a list of numbers in random that would consider the sequence at which we will
#fill the columns

fill_sequence = []
for i in range(8):
    fill_sequence.append(choice([k for k in range(8) if k not in fill_sequence]))
print(fill_sequence)

#at this point fill_sequence holds 8 unique numbers from 0 to 7
better = OpenSquareRegulator()
print(better.chessboard[1][0])
better.printboard()
