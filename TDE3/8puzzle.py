import time
import sys

'''
This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. 
The highest possible limit is platform- dependent.
'''
sys.setrecursionlimit(8192)

class PuzzleSolver():
    
    # Esse foi o exemplo dado na descrição do TDE
    initial_puzzle_state = [['8', '0', '6'],
                            ['5', '4', '7'],
                            ['2', '3', '1']]

    # Esse não tem solução
    # initial_puzzle_state = [['4', '7', '2'],
    #                         ['5', '3', '8'],
    #                         ['1', '0', '6']]

    expected_puzzle_state = '012345678'

    PUZZLE_SIZE = 9
    PUZZLE_COLS_ROWS = 3

    moves = 0

    def __init__(self, max_moves, use_table=False):
        self.max_moves = max_moves
        self.use_table = use_table
        self.states_dict = {}

        if use_table:
            self.states_table = [False for i in range(876543210)]


    def solve_puzzle(self):

        current_puzzle_state = self.initial_puzzle_state

        start_time = time.time()
        result = self.backtrack(0, 1, current_puzzle_state, 0)
        if result: 
            print("Puzzle resolvido em {:0.10f} segundos".format(time.time() - start_time))
        else:
            print("Nível máximo atingido")

    def backtrack(self, empty_row, empty_col , puzzle, level):
        '''
        Backtracking sinistro
        '''
        snapshot = self.take_puzzle_snapshot(puzzle)

        if self.state_already_visited(snapshot) or level > self.max_moves:
            return False

        self.save_puzzle_snapshot(snapshot)

        if snapshot == self.expected_puzzle_state:
            print(f"Resultado encontrado no nível {level}")
            print(puzzle)
            return True

        possible_moves = self.get_possible_moves(empty_row, empty_col)

        # itera sobre movimentos possíveis
        for move in possible_moves:
            new_row, new_col = move

            puzzle[empty_row][empty_col] = puzzle[new_row][new_col]
            puzzle[new_row][new_col] = '0'
            level +=1
            
            if self.backtrack(new_row, new_col, puzzle, level):
                return True
            
            puzzle[new_row][new_col] = puzzle[empty_row][empty_col]
            puzzle[empty_row][empty_col] = '0'

        return False

    def get_possible_moves(self, row, col):
        possible_moves = [] 

        if row > 0:
            possible_moves.append((row - 1, col))
        if col > 0:
            possible_moves.append((row, col - 1))
        if row < 2:
            possible_moves.append((row + 1, col))
        if col < 2:
            possible_moves.append((row, col + 1))

        return possible_moves

    def take_puzzle_snapshot(self, puzzle):
        '''
        Captura o estado do puzzle em uma string 
        '''

        size = self.PUZZLE_COLS_ROWS
        snapshot = ''

        for row in range(size):
            for col in range(size):
                snapshot += puzzle[row][col]
        
        return snapshot

    def save_puzzle_snapshot(self, snapshot):
        '''
        Salva o snapshot tirado do puzzle em
        um dicionário
        '''

        if self.use_table:
            self.states_table[int(snapshot)-1] = True

        else:
            self.states_dict[snapshot] = True

    def state_already_visited(self, snapshot):
        '''
        Verifica se estado já está presente
        no dicionário
        '''

        if self.use_table:
            if self.states_table[int(snapshot)-1]:
                return True
            else:
                return False

        else:
            if snapshot in self.states_dict:
                return True
            else:
                return False

if __name__ == '__main__':
    
    max_moves = 100

    # Com tabela
    # print("============== Com Tabela ==================")
    # solver1 = PuzzleSolver(max_moves, True)
    # solver1.solve_puzzle()
    
    # Com dicionário (hash map)
    print("============== Com Dicionário ==============")
    solver2 = PuzzleSolver(max_moves)
    solver2.solve_puzzle()