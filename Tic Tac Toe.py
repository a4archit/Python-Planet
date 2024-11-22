import numpy as np
import random 

class TicTacToe:
    
    def __init__(self):
        self.matrix = np.full((3,3), '.', dtype=str)
        
    def display(self):
        print()
        for row in self.matrix:
            for element in row:
                print("\t", element, end='')
            print()
        print()
        
    def set_value(self,player, r, c):
        value = 'X' if player == 1 else 'O'
        self.matrix[r,c] = value
    
    def get_blank_indices(self):
        indices = np.array(np.where(self.matrix == '.'))
        processed_indices = []
        for i in range(len(indices[0])):
            processed_indices.append((indices[0][i], indices[1][i]))
        return processed_indices
    
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
        


