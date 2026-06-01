import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Represents the 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Tells the user what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[0], self.board[4], self.board[8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[2], self.board[4], self.board[6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(state, player):
    max_player = 'O' # AI is 'O'
    other_player = 'X' if player == 'O' else 'O'

    # Base case: check if the previous move resulted in a win
    if state.current_winner == other_player:
        return {
            'position': None, 
            'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
        }
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    # Initialize dictionaries for tracking the best move
    if player == max_player:
        best = {'position': None, 'score': -math.inf} # Maximize AI score
    else:
        best = {'position': None, 'score': math.inf} # Minimize human score

    for possible_move in state.available_moves():
        # 1. Make a move
        state.make_move(possible_move, player)
        
        # 2. Recurse using minimax to simulate a game after making that move
        sim_score = minimax(state, other_player)

        # 3. Undo the move so we can test the next possible move
        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        # 4. Update the dictionary if necessary
        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
                
    return best