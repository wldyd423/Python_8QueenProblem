import numpy as np
import random as rd


class EightQueens:
    def __init__(self, size):
        self.size = size
        self.chessboard = np.zeros(self.size)
        self.count = 0

        for idx, position in enumerate(self.chessboard):
            self.chessboard[idx] = rd.randrange(0, self.size, 1)

    def hit_verbose(self, x, y, i):
        print(f"[{y}] Hit between line {x} and line {i}")

    def hit(self):
        self.count += 1

    def evaluate(self):
        print(self.chessboard)
        for x, y in enumerate(self.chessboard):
            for i in range(x+1, self.size):
                if(self.chessboard[i] == y):
                    self.hit()
                    # self.hit_verbose(x, "ide", i)
                    # print("hit")
                elif(self.chessboard[i] == y+i-x):
                    self.hit()
                    # self.hit_verbose(x, "upp", i)
                    # print("hit")
                elif(self.chessboard[i] == y-i+x):
                    self.hit()
                    # self.hit_verbose(x, "low", i)
                    # print("hit")
        return self.count


class GeneticAlgorithm:
    def __init__(self, population) -> None:
        self.population = population
        self.boardSize = 8
        self.verbose = True
        self.populate()

    def populate(self):
        for i in range(self.population):
            temp = EightQueens(self.boardSize)
            if self.verbose:
                print(temp.evaluate())


# e = EightQueens(8)
# print(e.evaluate())

set = GeneticAlgorithm(10)
