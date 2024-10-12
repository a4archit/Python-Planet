# data storing
import numpy as np
import pandas as pd
import sys

__doc__ = '''IDSS [1.0.8] Info Data Storing Software'''
exit_text = "Enter 'exit' for exiting"
initial_text = '''
Select option as your need:
    1. Log in
    2. Sign up
    3. Help(show data) - temp
    4. Exit
'''


def line(n=42):
    print('-'*n)


class Main:
    def __init__(self):
        self.database = np.array([
            ['archit', '2023', 'archit is pursue BCA'],
            ['vansh', 'asdf', 'vansh is a boy']
        ])
        self.datadf = pd.DataFrame(self.database)
        self.datadf.columns = ['Name', 'Password', 'Information']
        self.names_data = list(self.datadf.loc[:,'Name'])
            
        print(__doc__)
        while True:
            op = self.loop_inputs()
            if   op == 1: self.login_fx()
            elif op == 2: self.signup_fx()
            elif op == 3: print(self.datadf)
            else: sys.exit()
    
    def loop_inputs(self):
        __doc__ = '''
        On calling this function run a loop
        that take a number [1-4]
        '''
        print(initial_text)
        while True:
            try:
                uinput = int(input('>>> '))
            except:
                print('\nInvalid! Try Again\n')
                continue
            if (uinput > 0 and uinput <= 4):
                return uinput
                break
            else:
                print(f"\n'{uinput}' Invalid(1-4)")
    
    def signup_fx(self):
        # 1. input name and pass
        # 2. save to database
        while True:
            user_info = ''
            name = input('Enter your name: ').lower().strip()
            pswd = input('Enter password : ').lower().strip()
            if name=='' or pswd=='':
                print('Name or Password never be Empty')
                continue
            if name in self.names_data:
                print(f"{name} is already exsits\n\tTry with another Name")
                continue
            # updating dataframe of DataFrame
            self.datadf.loc[len(self.datadf.INDEX)] = [name, pswd, user_info]
            print(f"New user '{name.title()}' added successfully !!")
            # taking permission
            while True:
                permission = input('Do you want to signup with another account? (Y/N): ')
                if not permission:
                    print('Empty field is invalid !!!')
                    continue
                else:
                    break
            if permission in ['n','no','not','never','nahi','na']:
                break
                
        
 
    def login_fx(self):
        print(exit_text)
        while True:
            # Taking name and password
            name = input('\n--- Your name    : ').strip().lower()
            pswd = input('--- Your password: ').strip().lower()
            if not name or not pswd:
                print('Empty fields are not accepted.')
                continue
            
            if name in self.names_data:
                upswd = self.datadf.loc[self.datadf['Name']==name,  'Password']
                for i in range(3,0,-1):
                    print(f'Wrong Password\nYou have only({i}) chance(s).')
                    pswd = input('--- Your password: ').strip().lower()
                    if pswd != upswd.all():
                        continue
                    else:
                        print('Login Successfully')
                        break
                else:
                    print(f"Account Has Been Locked.")
                    return False
                uinfo = self.datadf.loc[self.datadf['Name']==name, 'Information']
                print(uinfo) # temporary
                # 1. see my information
                # 2. update my information
                # 3. clear my information
                
            else:
                print('no user found')
                continue
            while True:
                permission = input('Do you want to login with another account? (Y/N): ')
                if not permission:
                    print('Empty field is invalid !!!')
                    continue
                else:
                    break

            
    
    

if __name__ == "__main__":
    Main()








