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
        self.chessboard = [[1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1]]
    def reset(self):
        self.chessboard = [[1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1]]
    def printboard(self):
        for i in range(8):
            print(self.chessboard[i])
    def place(self, coord):
        #if given a coordinate at which a piece is place eliminate the attacking spots

        for i in range(8):
            self.chessboard[coord[0]][i] = 0
            self.chessboard[i][coord[1]] = 0
        mini = min(coord[0], coord[1])
        for i in range(1, mini + 1):
            self.chessboard[coord[0] - i][coord[1] - i] = 0
        mini = min(coord[0], 7 - coord[1])
        for i in range(1, mini + 1):
            self.chessboard[coord[0] - i][coord[1] + i] = 0
        mini = min(7 - coord[0], coord[1])
        for i in range(1, mini + 1):
            self.chessboard[coord[0] + i][coord[1] - i] = 0
        mini = min(7 - coord[0], 7 - coord[1])
        for i in range(1, mini + 1):
            self.chessboard[coord[0] + i][coord[1] + i] = 0


#make a list of numbers in random that would consider the sequence at which we will
#fill the columns

fill_sequence = []
for i in range(8):
    fill_sequence.append(choice([k for k in range(8) if k not in fill_sequence]))
print(fill_sequence)
print()
#at this point fill_sequence holds 8 unique numbers from 0 to 7
better = OpenSquareRegulator()

better.place((2, 4))
better.printboard()

for element in fill_sequence:
    print(element, end=' ')
    print(better.chessboard[element])

#Here we place a piece on the better.chessboard[element] first at placeit removing all the
#empty spaces
#within those empty spaces we place another piece
#if next iteration does not have any spaces left we go to previous and try another out
#eventually we will arrive at a solution!