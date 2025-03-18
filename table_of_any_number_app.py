# table of any number
# add exit button
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

class TableOfAnyNumber:
   
   def __init__(self):
      
      # app name
      name = tk.Label(root,
                      text = "Table of Number",
                      font = ("Courier", 15),
                      bg = "Grey",
                      fg = "white",
                      width = 21)
      name.place( x = 0, y = 0)
      
      # input 
      self.table = tk.Entry(root,
                           placeholder = 'Enter a number...',
                           width = 28,
                           border = 4,
                           relief = 'flat')
      self.table.place( x = 100, y = 200)
      
      # button
      btn = tk.Button(root,
                        text = "Write table now",
                        bg = 'grey',
                        fg = 'white',
                        width = 24,
                        command = self.table_fx)
      btn.place( x = 100, y = 300)
      
      root.mainloop()
      
   
   def table_fx(self):
      table_str = ""
      try :
         num = int(self.table.get())
      except :
         messagebox.showerror( None, 'Invalid Input')
         return False
      
      #messagebox.showinfo( None, 'success')
      
      i = 1
      while(i <= 10):
         table_str += f"{num: >12} × {i} = {num*i}\t\t\t\n"
         i += 1
      
      #messagebox.showinfo( None, 'success')
      
      # output label
      op = tk.Label( root,
                     text = f"\n\n{table_str}\n",
                     font = ('bold', 17),
                     bg = 'lightgrey')
      op.place( x = 0, y = 500)

      #messagebox.showinfo( None, 'success')


      
if __name__ == "__main__":
   
   TableOfAnyNumber()
   


