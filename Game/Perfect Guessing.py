""" 
Perfect Guessing Game
=====================

An amazing Game for small study break, full of joy.

"""

# import neccessary modules/functions
from typing import List
from random import randint

# some useful variables
general_instructions: str = '''
General Instructions:
    -> This is the number guessing game.
    -> This game guess numbers between (0-100).
    -> Player have infinite number of chances.
    -> On each chance player will enter the number between 0-100.
    -> If Player entered number is equal to the Computer's Numbers then the Player will be winner.
    -> Lesser the number of chances attempted demonstrate the Player winning quality.
    -> Enter 'exit' for closing the Game.
'''
initial_text: str = f"Welcome in Perfect Guessing Game (0.0.1)\n {general_instructions}"

def get_user_input(text: str, value_options: List[str | int] = ['y','n']) -> str:
    """ Return an element from value_options list after taking from user. """
    while True:
        user: str = input(f"\n{text}").lower().strip()
        if not user:
            print("Please give your input first.")
            continue
        if user == 'exit':
            print("Bye Bye")
            exit()
        if user in value_options:
            return user
        print(f"Invalid value: [{user}]\n\nValue must be from the given list -> {value_options}")

def perfect_guessing_game() -> None :
    """ Common/Main function for this Game. """
    # declaring and initialising some variables
    chance: int = 0
    range_list: List[int] = [ str(_) for _ in range(0,101)]
    computer_number: int = randint(0,100)
    message: str = ""
    inner_message: str = ""

    while True:
        chance += 1
        try:
            user_string = get_user_input(f"{'-'*50} Attempt: {chance}\nComputer number: ****\nYour guessed number(0-100): ",value_options=range_list)
            if user_string == 'exit':
                print("Bye Bye")
                exit()
            user_number = int(user_string)
        except:
            print("You doesn't enter properly. Try Again!")
            continue 
        # comparing the numbers
        if user_number == computer_number:
            message = f"\tHooryah!\n\tComputer number: {computer_number}\n\tYou are the winner, with {chance} attempts.\n"
            print(f"{message:>20} ")
            return
        else:
            inner_message = "higher" if user_number < computer_number else "lower"
            message = f"\tSo sad\t:(\n\tComputer number: ****\n\t{inner_message} number please."
        print(f"{message:>20} ")

def main() -> None :
    """ Main function """
    _match: int = 0
    print(initial_text)
    # taking player permission for start the game
    if get_user_input("Do you ready to play?\nAnswer(y/n): ") == 'n':
        print("Ok\nSee you next time.")
        exit()
    while True:
        _match += 1
        print(f"\n\n{'Match:'+str(_match):^50} ")
        perfect_guessing_game()
        if get_user_input("Do you want to play again?\nAnswer(y/n): ") in ['n','exit']:
            print("I hope you enjoy this game.\nThank you!")
            exit()




if __name__ == "__main__" :
    main()
