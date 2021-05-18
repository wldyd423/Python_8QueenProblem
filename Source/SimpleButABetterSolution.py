##Extension of Simple Solution.
##Still uses incremental formulation
## Book does acknowledge the existance of superior method but that would be made later

import SimpleSolution
import PySimpleGUI as sg
import ChessboardGUI as cg
import io
from PIL import Image
import random
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
        self.pieces = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
    def reset(self):
        self.chessboard = [[1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1]]
        self.pieces = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
    def pseudoreset(self):
        self.chessboard = [[1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1]]
    def printboard(self):
        print("Attack")
        for i in range(8):
            print(self.chessboard[i])
        print()
        print("Pieces")
        for i in range(8):
            print(self.pieces[i])
    def place(self, coord):
        #if given a coordinate at which a piece is place eliminate the attacking spots
        self.pieces[coord[0]][coord[1]] = 1
        self.scanallattack()

    def takeoff(self, col):
        for element in self.pieces[col]:
            if element == 1:
                self.pieces[col][self.pieces[col].index(element)] = 0
                self.scanallattack()
                return True
        return False

    def scanallattack(self):
        self.pseudoreset()
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j] == 1:
                    self.scanattack((i, j))

    def scanattack(self, coord):
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

    def checkemptycol(self, col):
        if 1 not in self.chessboard[col]:
            return False
        return True

    def makerange(self, col):
        temp = []
        loc = 0
        for element in self.chessboard[col]:
            if element == 1:
                temp.append(self.chessboard[col].index(element, loc))
                loc = self.chessboard[col].index(element, loc) + 1
        return temp

#make a list of numbers in random that would consider the sequence at which we will
#fill the columns

fill_sequence = []

for i in range(8):
    fill_sequence.append(choice([k for k in range(8) if k not in fill_sequence]))
print(fill_sequence)
print()
#at this point fill_sequence holds 8 unique numbers from 0 to 7
better = OpenSquareRegulator()

#better.place((2, 4))
#better.printboard()

"""print()
for element in fill_sequence:
    print(element, end=' ')
    print(better.chessboard[element], better.checkemptycol(element))"""

#Here we place a piece on the better.chessboard[element] first at placeit removing all the
#empty spaces
#within those empty spaces we place another piece
#if next iteration does not have any spaces left we go to previous and try another out
#eventually we will arrive at a solution!



"""col = 0
while 1:
    currange = better.makerange(col)
    if len(currange) == 0:
        break
    better.place((col, currange.pop()))
    col += 1

better.printboard()
"""
"""sol = 0
for col0 in better.makerange(0):
    better.place((0, col0))
    for col1 in better.makerange(1):
        better.place((1, col1))
        for col2 in better.makerange(2):
            better.place((2, col2))
            for col3 in better.makerange(3):
                better.place((3, col3))
                for col4 in better.makerange(4):
                    better.place((4, col4))
                    for col5 in better.makerange(5):
                        better.place((5, col5))
                        for col6 in better.makerange(6):
                            better.place((6, col6))
                            for col7 in better.makerange(7):
                                better.place((7, col7))
                                sol += 1
                                print(sol)
                                better.printboard()
                                better.takeoff(7)
                            better.takeoff(6)
                        better.takeoff(5)
                    better.takeoff(4)
                better.takeoff(3)
            better.takeoff(2)
        better.takeoff(1)
    better.takeoff(0)"""

better.place((1,1))
better.place((2,3))
better.printboard()
for i in range(8):
    print(better.makerange(i))