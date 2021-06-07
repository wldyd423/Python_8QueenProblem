class FitnessFunction:
    def __init__(self, length):
        self.solution = None
        self.length = length
        self.bestcase = 0
        for i in range(self.length):
            self.bestcase += i

    def get_bestcase(self):
        return self.bestcase

    def test_for_solution(self, boards):
        temp = self.bestboard(boards)
        if self.getscore(temp) == self.bestcase:
            self.solution = temp
            return True
        return False

    def getscore(self, board):
        score = 0
        for i in range(self.length):
            for j in range(i+1, self.length):
                if board[i] == board[j]:
                    score += 1
                elif board[i] + j - i == board[j]:
                    score += 1
                elif board[i] - j + i == board[j]:
                    score += 1
        return self.bestcase - score

    def bestboard(self, boards):
        maxindex = 0
        max = 0
        for i in range(4):
            if max < self.getscore(boards[i]):
                max = self.getscore(boards[i])
                maxindex = i
        return boards[maxindex]

    def getlist(self, boards):
        return {'board1': self.getscore(boards[0]),
                       'board2': self.getscore(boards[1]),
                       'board3': self.getscore(boards[2]),
                       'board4': self.getscore(boards[3])}

