import random

class Cell:
    
    def __init__(self, state, probability_mine):
        self.valid_states = {'', 'mine', 'empty', 'wiped'}
        self.probability_mine = probability_mine
        self.state = state if state in self.valid_states else self.generate_state()
        

    def generate_state(self):
        self.probability_empty = 10
        self.probability_x = 100 - self.probability_mine - self.probability_empty

        rand_num = random.randint(1, 100)

        if rand_num <= self.probability_empty:
            return 'empty'
        elif rand_num <= self.probability_empty + self.probability_mine:
            return 'mine'
        else:
            x_coefficient = 1 + (100 - rand_num) / 100.0
            x_coefficient = round(x_coefficient / 0.05) * 0.05
            return f'x_{x_coefficient:.2f}'
        
    def set_state(self, state):
        if state in self.valid_states:
            self.state = state
            return True
        else:
            print("Error: Incorrect state. See valids states: '', 'mine', 'empty', 'wiped'")
            return False

    def get_state(self):
        return self.state



