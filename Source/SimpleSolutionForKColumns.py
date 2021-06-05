import numpy as np


class KColumnChessBoard:
    def __init__(self, k):
        self.k = k
        self.attack = np.zeros((self.k, self.k)).astype(int).tolist()
        self.pieces = np.zeros((self.k, self.k)).astype(int).tolist()
        print("init!")
        self.sol = 0
        self.fir = 0
        self.valid_solution = None

    def getList(self):
        return self.pieces

    def reset_attack(self):
        self.attack = np.zeros((self.k, self.k)).astype(int).tolist()

    def reset_pieces(self):
        self.pieces = np.zeros((self.k, self.k)).astype(int).tolist()

    def print_board(self):
        print("Attack")
        for i in range(self.k):
            print(self.attack[i])
        print()
        print("Pieces")
        for i in range(self.k):
            print(self.pieces[i])

    def place(self, x, y):
        self.pieces[x][y] = 1
        self.scan_all_attack()

    def scan_all_attack(self):
        self.reset_attack()
        for i in range(self.k):
            for j in range(self.k):
                if self.pieces[i][j] == 1:
                    self.scan_attack(i, j)

    def scan_attack(self, x, y):
        for i in range(self.k):
            self.attack[x][i] = 1
            self.attack[i][y] = 1
        mini = min(x, y)
        for i in range(1, mini + 1):
            self.attack[x - i][y - i] = 1
        mini = min(x, self.k - 1 - y)
        for i in range(1, mini + 1):
            self.attack[x - i][y + i] = 1
        mini = min(self.k - 1 - x, y)
        for i in range(1, mini + 1):
            self.attack[x + i][y - i] = 1
        mini = min(self.k - 1 - x, self.k - 1 - y)
        for i in range(1, mini + 1):
            self.attack[x + i][y + i] = 1

    def make_range(self, col):
        ret = []
        loc = 0
        for element in self.attack[col]:
            if element == 0:
                ret.append(self.attack[col].index(element, loc))
                loc = self.attack[col].index(element, loc) + 1
        return ret

    def take_off(self, col):
        for element in self.pieces[col]:
            if element == 1:
                self.pieces[col][self.pieces[col].index(element)] = 0
                self.scan_all_attack()
                return True
        return False

    def brutal_solution(self, col):
        if col == self.k:
            return True
        for col_temp in self.make_range(col):
            #self.print_board()
            self.place(col, col_temp)
            if col + 1 == self.k:
                self.print_board()
                self.sol += 1
            self.brutal_solution(col + 1)
            self.take_off(col)

    def find_first_solution(self, col):
        if self.fir == 1:
            return True
        for col_temp in self.make_range(col):
            #self.print_board()
            self.place(col, col_temp)
            if col + 1 == self.k:
                self.print_board()
                self.fir = 1
                ret = []
                x = 0
                for element in self.pieces:
                    ret.append((x, element.index(1)))
                    x+=1
                print(ret)
                self.valid_solution = ret
                print(self.valid_solution)
                return ret
            self.find_first_solution(col + 1)
            self.take_off(col)


"""better = KColumnChessBoard(20)
better.find_first_solution(0)
print(better.sol)"""