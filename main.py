from tictactoe import TicTacToe, minimax
import time

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # Human starts first
    while game.empty_squares():
        if letter == 'O':
            # AI's turn
            print("\nAI is thinking...")
            time.sleep(0.5) # Slight delay to simulate thinking
            square = minimax(game, letter)['position']
        else:
            # Human's turn
            valid_square = False
            val = None
            while not valid_square:
                square = input(f'\n{letter}\'s turn. Input move (0-8): ')
                try:
                    val = int(square)
                    if val not in game.available_moves():
                        raise ValueError
                    valid_square = True
                except ValueError:
                    print('Invalid square. Try again.')
            square = val

        # Execute the move
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()

            if game.current_winner:
                if print_game:
                    print(f'\n*** {letter} WINS! ***')
                return letter
            
            # Switch players
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('\nIt\'s a tie!')

if __name__ == '__main__':
    print("==============================================")
    print("Welcome to Tic-Tac-Toe against the Minimax AI!")
    print("==============================================")
    print("You are 'X' and the AI is 'O'.")
    print("Enter a number between 0 and 8 to place your mark.\n")
    
    game = TicTacToe()
    play(game, 'X', 'O', print_game=True)