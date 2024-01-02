from Cell import Cell

class Board:
    def __init__(self, rows, columns, probability_mine):
        self.rows = rows
        self.columns = columns
        self.probability_mine = probability_mine
        self.grid = [[Cell(None, probability_mine) for _ in range(columns)] for _ in range(rows)]

    def display_board(self):
        for row in self.grid:
            for cell in row:
                print(cell.get_state(), end='\t')
            print()
            
    def get_cell_state(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            return self.grid[row][col].get_state()
        else:
            print("Error: Incorrect coordinates. Expected format x, y")
            return None
        
    def set_cell_state(self, row, col, state):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.grid[row][col] = Cell(state, self.probability_mine)
        else:
            print("Error: Incorrect coordinates. Expected format x, y")
            return None

    def count_mines(self):
        mine_count = sum(cell.get_state() == 'mine' for row in self.grid for cell in row)
        return mine_count
