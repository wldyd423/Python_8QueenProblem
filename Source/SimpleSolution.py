#States: Any arrangement of 0 to 8 queens on the board is a state
#Initial state: No queens on the board.
#Actions: add a queen to any empty square
#Transition model: Return the board with a queen added to the specified square
#Goal test: 8 queens are on the board, none attacked.

import Debugging
db = Debugging.SimpleDebuger()
db.DEBUG_ON = False


class SimpleSolution:
    def __init__(self):
        self.queen_position = [-1, -1, -1, -1, -1, -1, -1, -1]

    def check_attack(self):
        for i in range(8):
            for j in range(i + 1, 8):
                db.simple_print(f"{i} {j}")
                if self.queen_position[i] == -1:
                    return True
                if self.queen_position[i] == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print("false1")
                    return False
                elif self.queen_position[i] + j - i == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print("false2")
                    return False
                elif self.queen_position[i] - j + i == self.queen_position[j] \
                        and self.queen_position[j] != -1:
                    db.simple_print("false3")
                    return False
        return True

    def force_set(self, arr):
        if len(arr) == 8:
            self.queen_position = arr

    def append_queen(self, pos):
        for element in self.queen_position:
            if element == -1:
                element = pos
                return True
        return False


d = SimpleSolution()
d.force_set([1,3,5,7,4,-1,-1,-1])
print(d.check_attack())