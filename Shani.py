# My First Bot

# import one tk file in another tk file and use code of one in another

import tkinter as tk
from tkinter import messagebox
from tkinter import * 
from tkinter.ttk import *
import nltk
from nltk.chat.util import Chat, reflections
import datetime
from datetime import date
from datetime import time
from time import time, sleep

root = tk.Tk()
root.config( bg = 'white')

class Bot:
   def __init__(self):
      
      # menu bar
      menubar = Menu(root) 

      
      # Adding File Menu and commands 
      file = Menu(menubar, tearoff = 0) 

      menubar.add_cascade(label =' +  ', menu = file, font = ('bold', 20))
      file.add_command(label ='About us', font=('bold',10), command = self.about_fx)
      file.add_command( label = 'Contact us', font=('bold',10), command = self.contact_fx)
      file.add_separator()
      file.add_command(label ='Exit', font=('bold',10), command = root.destroy) 
      root.config(menu = menubar)
      
      menubar.add_cascade( label=" \t Shani ", font = ('bold', 15))
      
      # 'chating': label
      chating_label = tk.Label(root,
                      text = " Let`s chat...",
                      font = ("Courier", 10),
                      width = 35,
                      height = 2,
                      bg = 'white',
                      anchor = 'w',
                      border = 0,
                      relief = 'solid')
      chating_label.place( x = 0, y = 40)
      
      # QUIT: Button
      back = Button( root, 
                     text = " QUIT ", 
                     command = root.destroy,
                     width = 15)
      back.place(x = 410, y = 10, height = 65)
      
      # user name: input
      self.user_name = tk.Entry(root,
                                placeholder = ' Your name',
                                border = 1,
                                width = 15,
                                relief = 'sunken')
      self.user_name.place( x = 410, y = 80, height = 65)
      
      # scroll bar
      self.scrollbar = tk.Scrollbar(root, width = 38)
      self.scrollbar.pack( side = RIGHT, fill=Y, padx = 0, pady = 160)
      
      # Output Text
      self.output = tk.Text(root,
                           bg = 'white',
                           fg = 'black',
                           height = 30,
                           width = 42,
                           border = 0,
                           wrap = 'word',
                           yscrollcommand = self.scrollbar.set)
      self.output.pack( side = LEFT, fill = BOTH )
      self.output.place( x = 0, y = 160, width = 675, height = 1000)
      self.output.configure( font = ('imprint mt shadow', 8))
      sn = '\n'
      self.output.insert(tk.END, f'{sn*12}\tLet`s chat with shani...{sn*12}')
      self.bot("Hello, how can I assist you today?")
      self.output.config( state = DISABLED)
      self.output.yview('end')
      self.scrollbar.config( command = self.output.yview )
            
      # input: entry
      self.input_entry = tk.Entry(root,
                                  placeholder = ' Enter message...',                            
                                  font = ('bold', 10))
      self.input_entry.place( x = 30, y = 1170, height = 100, width = 450)
      
      # send button
      send_btn = tk.Button(root,
                           text = ' Send ',
                           width = 5,
                           bg = 'white',
                           bd = 4,
                           relief = 'groove',
                           command = self.next_btn_fx)
      send_btn.place( x = 500, y = 1170, height = 100)
      
      # developer line
      dl = tk.Label(
                  root,
                  text = '- Developed by Archit Tyagi',
                  bg = 'white',
                  font = ('Times', 8))
      dl.place(x = 120, y = 1350)
      
      root.mainloop()

# ------------- About Window ---------------------------------------------
   def about_fx(self):
      window = tk.Tk()
      
      window.geometry('670x1000')
      window.title('About us')
      window.config( bg = 'white')
      
      # heading
      heading = tk.Label( window,
                           text = "About us",
                           font = ("bold", 10),
                           bg = 'white')
      heading.pack( padx = 20, pady = 30)
      user_name = self.user_name.get().strip().capitalize()
      
      # about
      about = tk.Label( window,
         text = 
f"""Hello dear {user_name},
As we know about this technical world and its 
different types of technology.

We are junior learners, always try to learning
in the field of IT i.e. new skill or new things
related to our career.
""",
         font = ('Arial', 7),
         bg = 'white',
         justify = LEFT)
      about.pack( padx = 20, pady = 0, anchor = "w")
      
      # heading: About Archit
      heading2 = tk.Label( window,
                           text = "About Archit",
                           font = ("bold", 10),
                           bg = 'white',
                           justify = LEFT)
      heading2.pack( padx = 20, pady = 50, anchor = "w")
           
      # details: About Archit
      about_archit = tk.Label( window,
         text = 
f"""This program is created by Archit Tyagi

Education : 
   UG   - BCA 1 year (2023)
   12th - 79.4% CBSE (DPM Sr. Sec Public School)
   10th - 72.4% CBSE (DPM Sr. Sec Public School)

""",
         font = ('Arial', 7),
         bg = 'white',
         justify = LEFT)
      about_archit.pack( padx = 20, pady = 0, anchor = "w")
      
      # Button: contact to Archit
      cta_btn = Button( window,
                        text = " Contact to Archit ",
                        command = self.contact_fx,
                        width = 15)
      cta_btn.pack( padx = 5, pady = 10)
      
      # Button
      back = Button( window, 
                     text = " Back ", 
                     command = window.destroy,
                     width = 15)
      back.pack( padx = 5, pady = 10)
      
      window.mainloop()

# -------------- Contact Window----------------------------------------------------   
   def contact_fx(self):
      window = tk.Tk()
      
      window.geometry('600x600')
      window.title('Contact us')
      window.config( bg = 'white')
      # heading
      heading = tk.Label( window,
                           text = "Contact Details",
                           font = ("bold", 10),
                           bg = 'white')
      heading.pack( padx = 20, pady = 30)
      
      # details
      details = tk.Label( window,
         text = """
Address : Meerut, Uttar Pradesh
Email   : arcxxxxxxxx@gmail.com
Phone   :  +91 733827XXXX 
           +91 973783XXXX
         """,
         font = ('courier', 7),
         justify = LEFT,
         bg = 'white')
      details.pack( padx = 20, pady = 80)
      
      # Button
      back = Button( window, 
                     text = " Back ", 
                     command = window.destroy,
                     width = 15)
      back.pack( padx = 5, pady = 10)
      
      
      window.mainloop()

# ---------- Some functions use in code 
                        
   def msg(self, m):
      messagebox.showinfo(None, m)
   
   def bot(self, text):
      bot_name = '~ Shani :'
      sleep(.1)
      self.output.insert(tk.END, f'\n\n{bot_name} \t {text.capitalize()}\n')

# ******************  main  ************************
   def next_btn_fx(self):
      
      
      # enable output box for editing text
      self.output.config( state = tk.NORMAL)
      
      # take some data for useful information
      today_date = date.today()
      
      # setting user name
      user_name = self.user_name.get()
      if user_name == "":
         user_name = 'you'
      
      self.user_input = self.input_entry.get().lower().strip()
      
      text_list = self.user_input.split(' ')
      
      patterns = [
         (r'name|(.*) your name(.*)', ['my name is shani|','My self shani']),
         (r'shani|hello shani|hi shani|hello|hey|hi|hii', ['Hello, How you feel today?']),
         (r'(.*) happy|happy|best| very happy|very happy| awesome|awesome| well|well| very well|very well| good|good| nice|nice(.*)', ['Wow! I hope you will happy whole life']),
         (r'bad|ugly|very bad',['Don`t worry try to be happy']),
         (r'about you|about shani|i don\'t know about you|descibe yourself|define yourself', ['My self \'Shani\', made by archit\'s team.\nI am a software coded in Python programming language. I am here for you.']),
         (r'(.*)how are you(.*)', ['I am good, thanks!', 'I am doing well.']),
         (r'(.*)thank|thanks|thank you|you are best|you are helpful(.*)', ['Welcome! I am happy']),
         (r'(.*)bye|goodbye(.*)', ['Goodbye!', 'See you later!']),
         (r'(.*) months|month|month name|months name|month names|months names (.*)', ['january\n\tfebruary\n\tmarch\n\tapril\n\tmay\n\tjune\n\tjuly\n\taugust\n\tseptember\n\tnovember\n\tdecember'.title()]),
         (r'days|(.*)day names|days names|days name(.*)', ['sunday\n\tmonday\n\ttuesday\n\twednesday\n\tthrusday\n\tfriday\n\tsaturday'.title()]),
         (r'fruit|(.*) fruit list|fruits|fruits list|fruit name|fruit name list|fruits names|fruit names|fruits names(.*)', ['mango\n\tgrapes\n\tguavava\n\torange\n\tpine apple\n\tapple'.title()]),
         (r'(.*) can i help you(.*)', ['Oh! Thanks, but here i am your assistant']),
         (r'(.*) fuck(.*)', ['Mind your language!', 'Don`t use unapropriate words like `Fuck`.']),
         (r'(.*) help me| help us(.*)', ['Hey you can say now, How can i help you(.*)']),
         (r'(.*) sorry| so sad(.*)', ['Don`t worry']),
         (r'(.*) help you(.*)', ['Thank you!']),
         (r'(.*) are you mad|you are mad(.*)', ['No', 'Never', 'No yet']),
         (r'(.*) hindi numbers|hindi numbers| numbers in hindi|numbers in hindi| hindi counting', ['\n\t0-० \n\t1-१ \n\t2-२ \n\t3-३ \n\t4-४ \n\t5-५ \n\t6-६ \n\t7-७ \n\t8-८ \n\t8-9']),
         (r'(.*) you speak in hindi|you speak in hindi|you speaks hindi', ['Sorry, I can\'t understand hindi', 'So sorry, but I am unable to understand hindi']),
         (r'(.*) oh|oh(.*)', ['Don\'t worry']),
         (r'(.*) your developer|your developer|who creates you|your creator|your creater|who makes you(.*)', ['Archit Tyagi mades me', 'I am developed by Archit Tyagi']),
         (r'(.*) when developed you| when develop you| when you created| ',['I am developed in oct 2023', 'Beggining oct 2023']),
         # here start variables use in chating for more interesting 
         (r'(.*) today date|today date|date today(.*)|today date', [f'{today_date}']),
         (r'(.*) open google|open google|google.com', [f'opening google.com f{open_site("https://www.google.com/")}'])      
           
      ]
      
      
      # Create a Chat object with patterns and reflections
      try:
         chatbot = Chat(patterns, reflections)
      except _tkinter.TclError as err:
         pass
      
        
      # Start the chatbot interaction
      while True:
          
          if self.user_input == "":
             self.msg('enter something first')
             break
          self.output.insert( tk.END, f'\n\n~ {user_name.title()} :\t {self.user_input.capitalize()}\n')
          
          if self.user_input == 'bye':
              self.bot("Goodbye!")
              break
          else:
              response = chatbot.respond(self.user_input)
              if response is None:
                 self.bot("I'm not sure I understand. Please rephrase your question.")
                 break
              self.bot(response)
              break
      
      # disabled output box
      self.output.config( state = DISABLED)
      
      self.output.yview('end')
      
      # clear input bar
      self.input_entry.delete(0, tk.END)
   # ------ Next btn code ends here


def open_site(url: str) -> None:
    pass



# testing-
if __name__ == "__main__":
   Bot()
   
