import numpy as np
import random 

class TicTacToe:
    
    def __init__(self):
        self.matrix = np.full((3,3), None)
        
    def display(self):
        print()
        for row in self.matrix:
            for element in row:
                element_msg = 'X' if element == 1 else 'O' if element == 0 else '.'
                print("\t", element_msg, end='')
            print()
        print()
    
    def get_numeric_matrix(self):
        pass
        
    def set_value(self,player, r, c):
        value = 1 if player == 1 else 0
        self.matrix[r,c] = value
    
    def get_blank_indices(self):
        indices = np.array(np.where(self.matrix == None))
        processed_indices = []
        for i in range(len(indices[0])):
            processed_indices.append((indices[0][i], indices[1][i]))
        return processed_indices
        
    def check_winning(self):
        check_winning_rows_()
        
    def check_winning_(self, action_on: str) -> str:
        match(action_on):
            case 'rows':
                for row in self.matrix:
                    if""
            case 'columns':
                pass
            case 'diagnols':
                pass
            case _ :
                raise('Invalid value of \'action_on\'')
    
    # --------- end of class 'TickTacToe' ------------ #
    
def clean_user_choice(user_choice):
    return [int(element)-1 for element in user_choice.split(',')]




if __name__ == "__main__":
    
    game = TicTacToe()
    
    while True:
        game.display()
        user_choice = input('Player 1: ')
        r1, c1 = clean_user_choice(user_choice)
        game.set_value(1, r1, c1)
        blank_indices = game.get_blank_indices()
        computer_choice = random.choice(blank_indices)
        r2, c2 = computer_choice
        game.set_value(2, r2, c2)
        


