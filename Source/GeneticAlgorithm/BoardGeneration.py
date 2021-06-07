import random


class KQueens:
    def __init__(self, k):
        self.k = k
        self.board1 = [random.randint(0, self.k - 1) for n in range(self.k)]
        self.board2 = [random.randint(0, self.k - 1) for n in range(self.k)]
        self.board3 = [random.randint(0, self.k - 1) for n in range(self.k)]
        self.board4 = [random.randint(0, self.k - 1) for n in range(self.k)]
        self.past1 = None
        self.past2 = None
        self.past3 = None
        self.past4 = None

    def get_boards(self):
        return [self.board1, self.board2, self.board3, self.board4]

    def print_boards(self):
        print("Board State")
        print(self.board1)
        print(self.board2)
        print(self.board3)
        print(self.board4)
        print()

    def selection(self, fitness_score):
        self.past1 = self.board1[:]
        self.past2 = self.board2[:]
        self.past3 = self.board3[:]
        self.past4 = self.board4[:]
        fitness = [list(fitness_score.values())[0], list(fitness_score.values())[1],
                     list(fitness_score.values())[2], list(fitness_score.values())[3]]
        total = list(fitness_score.values())[0] + list(fitness_score.values())[1] + list(fitness_score.values())[2] + list(fitness_score.values())[3]
        fitness = [round(x/total, 2) for x in fitness]
        print(fitness)
        rand = random.choices(
            population=[list(fitness_score.keys())[0], list(fitness_score.keys())[1],
                        list(fitness_score.keys())[2], list(fitness_score.keys())[3]],
            weights=fitness,
            k=4
        )

        #print(rand)
        if rand[0] == 'board2':
            self.board1 = self.past2[:]
        elif rand[0] == 'board3':
            self.board1 = self.past3[:]
        elif rand[0] == 'board4':
            self.board1 = self.past4[:]

        if rand[1] == 'board1':
            self.board2 = self.past1[:]
        elif rand[1] == 'board3':
            self.board2 = self.past3[:]
        elif rand[1] == 'board4':
            self.board2 = self.past4[:]

        if rand[2] == 'board1':
            self.board3 = self.past1[:]
        elif rand[2] == 'board2':
            self.board3 = self.past2[:]
        elif rand[2] == 'board4':
            self.board3 = self.past4[:]

        if rand[3] == 'board1':
            self.board4 = self.past1[:]
        elif rand[3] == 'board2':
            self.board4 = self.past2[:]
        elif rand[3] == 'board3':
            self.board4 = self.past3[:]

        #self.print_boards()
    def cross_over_all(self):
        point = random.randint(1, self.k - 1)
        point2 = random.randint(1, self.k - 1)
        self.cross_over(1, point, point2)

    def cross_over(self, set, point, point2):
        frac1 = []
        frac2 = []
        frac3 = []
        frac4 = []
        #board1 and board2
        for i in range(point, self.k):
            frac1.append(self.board1[i])
            frac2.append(self.board2[i])
        #print(frac1)
        #print(frac2)
        for i in range(len(frac1)):
            self.board1[point+i] = frac2[i]
            self.board2[point+i] = frac1[i]

            #board3 and board4
        for i in range(point2, self.k):
            frac3.append(self.board3[i])
            frac4.append(self.board4[i])
        #print(frac3)
        #print(frac4)
        for i in range(len(frac3)):
            self.board3[point2+i] = frac4[i]
            self.board4[point2+i] = frac3[i]

    def mutation(self):
        mut1 = random.randint(0, self.k)
        mut2 = random.randint(0, self.k)
        mut3 = random.randint(0, self.k)
        mut4 = random.randint(0, self.k)

        if mut1 < self.k:
            self.board1[mut1] = random.randint(0, self.k - 1)
        if mut2 < self.k:
            self.board2[mut2] = random.randint(0, self.k - 1)
        if mut3 < self.k:
            self.board3[mut3] = random.randint(0, self.k - 1)
        if mut4 < self.k:
            self.board4[mut4] = random.randint(0, self.k - 1)