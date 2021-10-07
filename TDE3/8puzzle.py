import sys
'''
This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. 
The highest possible limit is platform- dependent.
'''
sys.setrecursionlimit(8192)

class PuzzleSolver():
    
    states_dict = {}

    initial_puzzle_state = [['8', '0', '6'],
                            ['5', '4', '7'],
                            ['2', '3', '1']]

    expected_puzzle_state = '012345678'

    PUZZLE_SIZE = 9
    PUZZLE_COLS_ROWS = 3
    possible_moves = [(1, 0), (-1, 0), (0, 1), (0,-1)]

    moves = 0

    def __init__(self, max_moves):
        self.max_moves = max_moves

    def solve_puzzle(self):

        current_puzzle_state = self.initial_puzzle_state

        self.backtrack(0, 1, current_puzzle_state, 0)
        print("Acabou")


    def backtrack(self, empty_row, empty_col , puzzle, level):
        '''
        Backtracking sinistro
        '''
        snapshot = self.take_puzzle_snapshot(puzzle)
        
        if self.state_already_visited(snapshot) or level > self.max_moves:
            return False

        self.save_puzzle_snapshot(snapshot)

        if snapshot == self.expected_puzzle_state:
            print("Achei")
            return True

        # itera sobre movimentos possíveis
        for move in self.possible_moves:

            row_move = move[0] + empty_row
            if row_move < 0 or row_move > 2: # movimento inválido
                continue

            col_move = move[1] + empty_col
            if col_move < 0 or col_move > 2: # movimento inválido
                continue
            
            # faz movimento
            print(puzzle[empty_row][empty_col])
            puzzle[empty_row][empty_col] = puzzle[row_move][col_move]
            puzzle[row_move][col_move] = '0'
            print(puzzle)

            level += 1
            if self.backtrack(row_move, col_move, puzzle, level):
                return True
        
        return False

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
        self.states_dict[snapshot] = True

    def state_already_visited(self, snapshot):
        '''
        Verifica se estado já está presente
        no dicionário
        '''
        if snapshot in self.states_dict:
            return True
        else:
            return False

if __name__ == '__main__':
    solver = PuzzleSolver(100)
    solver.solve_puzzle()