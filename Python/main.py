from ast import List
import random as rd
import numpy as np

chessboard = np.zeros(8)

print(chessboard)

for idx, position in enumerate(chessboard):
    chessboard[idx] = rd.randrange(0, 8, 1)

print(chessboard)
