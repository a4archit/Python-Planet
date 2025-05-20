import numpy as np
import random 


# main class
class TicTacToe:
    
    def __init__(self, mode: str):
        player2 = 'comp' if mode == 'comp' else 'user'
        self.matrix = np.full((3,3), None)
        self.player1_chance = 0
        self.player2_chance = 0
        self.total_chances = self.player1_chance + self.player2_chance
        
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
        
    def check_winner(self):
        winning_possibilities = ['rows', 'columns', 'diagnols']
        for winning_possibility in winning_possibilities:
            winner = self.check_winning_(winning_possibility)
            if winner is not None:
                break
        return winner      
        
        
    def check_winning_(self, action_on: str) -> str:
        match(action_on):
            case 'rows':
                for row in self.matrix:
                    msg = ('p1' if row.all() == 1 else 
                          'p2' if row.all() == 0 else None)
                    break
                return msg
                
            case 'columns':
                for col_index in range(self.matrix.shape[1]):
                    column = self.matrix[:,col_index]
                    msg = ('p1' if column.all() == 1 else 
                          'p2' if column.all() == 0 else None)
                    break
                return msg
                
            case 'diagnols':
                msg = ('p1' if np.diag(self.matrix).all() == 1 else
                      'p2' if np.diag(self.matrix).all() == 0 else None)
                
                if msg == 'None':
                    msg = ('p1' if np.diag(np.fliplr(self.matrix)).all() == 1 else
                          'p2' if np.diag(np.fliplr(self.matrix)).all() == 0 else None)
                return msg
                
            case _ :
                raise('Invalid value of \'action_on\'')
    
    # --------- end of class 'TickTacToe' ------------ #
    
def clean_user_choice(user_choice):
    return [int(element)-1 for element in user_choice.split(',')]




if __name__ == "__main__":
    
    game = TicTacToe(mode='comp')
    
    while True:
        game.display()
        user_choice = input('Player 1: ')
        r1, c1 = clean_user_choice(user_choice)
        game.set_value(1, r1, c1)
        blank_indices = game.get_blank_indices()
        computer_choice = random.choice(blank_indices)
        r2, c2 = computer_choice
        game.set_value(2, r2, c2)
        print("winner -> ", game.check_winner())
        


