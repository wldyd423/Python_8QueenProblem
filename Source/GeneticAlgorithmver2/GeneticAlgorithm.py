import numpy as np

test = np.random.randint(8, size = (8, 10))
#print(test)

def fitness(board):
    #print(len(board))   -- 8
    score = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                score += 1
            elif board[i] == board[j] + j - i:
                score += 1
            elif board[i] == board[j] - j + i:
                score += 1
    return score

#print(fitness(test[0]))

class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population
        self.board = np.random.randint(8, size = (self.population, 8))
        self.fitnessScore = np.zeros(self.population)
        self.probability = np.zeros(self.population)
        self.nextboard = np.zeros((self.population, 8))
        self.solution = -1
        #print(self.board)
        #print(self.fitnessScore)
    
    def fitness(self):
        for i in range(self.population):
            self.fitnessScore[i] = 28 - fitness(self.board[i])
        print(self.fitnessScore)
        #print(np.sum(self.fitnessScore))
        for i in range(self.population):
            self.probability[i] = self.fitnessScore[i] / np.sum(self.fitnessScore)
        #print(self.probability)
        #print(np.sum(self.probability))
        
    def mix(self, a, b):
        return np.append(a[4:], b[:4])

    def mutate(self):
        for i in range(self.population):
            for j in range(8):
                if np.random.choice([0,1], p = [0.95, 0.05]) == 1:
                    self.nextboard[i][j] = np.random.randint(8)

    def naturalSelection(self):
        for i in range(self.population):
            first = np.random.choice(np.arange(self.population), p = self.probability)
            second = np.random.choice(np.arange(self.population), p = self.probability)
            
            self.nextboard[i] = np.copy(self.mix(self.board[first], self.board[second]))
            
            self.mutate()
        self.board = np.copy(self.nextboard)
        self.nextboard = np.zeros((self.population, 8))

    def checkSolution(self):
        if max(self.fitnessScore) == 28:
            print(self.fitnessScore)
            print(self.board)
            return True
        return False

X = GeneticAlgorithm(20)
while 1:
    X.fitness()
    if X.checkSolution():
        break
    X.naturalSelection()