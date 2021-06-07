from Source.GeneticAlgorithm import BoardGeneration as bg
from Source.GeneticAlgorithm import FitnessFunction as ff


board = bg.KQueens(8)
fitness = ff.FitnessFunction(8)



while 1:
    boards = board.get_boards()
    print(fitness.get_bestcase())
    print(fitness.getlist(boards))
    print("=======start========")
    board.selection(fitness.getlist(boards))
    board.print_boards()
    board.cross_over_all()
    board.print_boards()
    board.mutation()
    board.print_boards()
    print("====end========")
    print(fitness.getlist(boards))
    if fitness.test_for_solution(boards):
        print("FoundSolution")
        print(fitness.solution)
        break

