"""
Snake Water Gun :
===============

This is the game Snake Water Gun.
There are three Elements Snake, Water and Gun. Let's discuss some rules.
    1. Water Destroy the gun
    2. Gun Kill the Snake
    3. Snake drink the water

Let's see its winning system

+----------------------------+
| Player | Computer | Winner |
+--------+----------+--------+
| Snake  | Gun      | C      | 
| Snake  | Water    | P      |
| Snake  | Snake    | -      |
| Water  | Snake    | C      |
| Water  | Gun      | P      |
| Water  | Water    | -      |
| Gun    | Water    | P      |
| Gun    | Snake    | C      |
| Gun    | Gun      | -      |
+--------+----------+--------+
"""

initial_text: str = '''
Welcome in SGW 2.0.21
------ Game ---------

Instructions:
1. Enter S for Snake
2. Enter G for Gun
3. Enter W for Water
4. Enter E for closing the Game
'''

from random import choice

# Global variables
options_list: list = ['s','g','w','e']

def take_valid_input() -> str:
    ''' Returns the valid user_option input '''
    while True:
        try:
            user_option: str = input("\n\n Enter an option: ").lower().strip()
        except:
            print("Please enter an option first")
            continue
        if user_option not in options_list:
            print(f"Wrong Option: Read Instruction carefully")
            continue
        return user_option

def computer_option() -> str:
    ''' return an option from the options list randomly '''
    computer_options_list: list = options_list[:-1]
    computer_option: str = choice(computer_options_list)
    return computer_option

def main() -> None:
    """ Main Function """
    print(initial_text)
    result: str = "" # d-draw, w-win, l-lose
    while True:
        user_option: str = take_valid_input()
        comp_option: str = computer_option()
        match user_option:
            case _ if user_option == comp_option:
                result = "d"
            case _ if user_option == 's':
                result = 'w' if comp_option == 'w' else 'l'
            case _ if user_option == 'w':
                result = 'w' if comp_option == 'g' else 'l'
            case _ if user_option == 'g':
                result = 'w' if comp_option == 's' else 'l'
            case _ :
                print("See You next time.")
                break

        result_text: str = 'you won' if result == 'w' else 'you lose' if result == 'l' else 'match draw'
        print(f"Computer option: {comp_option}\n---> {result_text.title()}")
            


if __name__ == "__main__" :
    main()

