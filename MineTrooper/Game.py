from Board import Board
from Bank import Bank

class Game:
    def __init__(self, rows, columns, probability_mine, initial_balance):
        self.board = Board(rows, columns, probability_mine)
        self.bank = Bank(initial_balance)

    def display_board(self):
        self.board.display_board()

    def open_cell(self, row, col):
        cell_state = self.board.get_cell_state(row, col)
        
        if cell_state is None:
            print("Error: Cell state is None. Check your coordinates.")
            return

        if cell_state == 'mine':
            self.bank.Reduce(self.bank.get_balance())
            print("Mine! You lost all your money.")
        elif cell_state.startswith('x_'):
            coefficient = float(cell_state.split('_')[1])
            self.bank.Deposit(self.bank.get_balance() * coefficient)
            print(f"Multiplier! Your bank is now {self.bank.get_balance()}")
        elif cell_state == 'empty':
            print("Empty cell. Nothing happens.")
        elif cell_state == 'wiped':
            print("Cell already opened. Choose another one.")
        else:
            print("Invalid cell state.")

        self.board.set_cell_state(row, col, 'wiped')

    def get_bank_balance(self):
        return self.bank.get_balance()

    def is_game_over(self):
        return self.bank.get_balance() <= 0
    
