import numpy as np
import random as rd


class EightQueens:
    def __init__(self, size):
        self.size = size
        self.chessboard = np.zeros(self.size)

        for idx, position in enumerate(self.chessboard):
            self.chessboard[idx] = rd.randrange(0, self.size, 1)

    def hit(self, x, y, i):
        print(f"[{y}] Hit between line {x} and line {i}")

    def evaluate(self):
        print(self.chessboard)
        for x, y in enumerate(self.chessboard):
            for i in range(x+1, self.size):
                if(self.chessboard[i] == y):
                    self.hit(x, "ide", i)
                    # print("hit")
                elif(self.chessboard[i] == y+i-x):
                    self.hit(x, "upp", i)
                    # print("hit")
                elif(self.chessboard[i] == y-i+x):
                    self.hit(x, "low", i)
                    # print("hit")


e = EightQueens(8)
e.evaluate()
