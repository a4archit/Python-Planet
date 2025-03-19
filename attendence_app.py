############################################
#   
#   ~ ARCHIT TYAGI
#   
#   Total Time Spend: 5 hrs
#
############################################


import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import *

root = tk.Tk()

class AttendenceApp:
   def __init__(self):
      
      root.attributes("-fullscreen",True)
      
      # app name
      app_name = tk.Label(root, text="Attendence Register", font=("bold", 15)).place(x=50, y=50)
      
      # about
      about_str = "This software helps teachers to take attendence digitally"
      about_btn = tk.Button(root, text = "About", command = lambda:
         messagebox.showinfo('About', about_str))
      
      # developed by archit tyagi: label
      archit = tk.Label(root, text = "- developed by Archit Tyagi").place(x=150, y=1400)
      
      # select section
      sec_list = [
         'Sec A',
         'Sec B',
         'Sec C'
      ]
      self.sec_options = tk.StringVar(root)
      self.sec_options.set(sec_list[0])
      self.sec_input = tk.OptionMenu(root, self.sec_options, *sec_list)
      self.sec_input.place(x=30, y=150)
            
      # Today Attendence
      attendence = tk.Button(root, text="Start Attendence", width=35, command=self.today_attendence_fx).place(x=30, y=300)
      
      root.mainloop()

# -------------------------------- Today Attendence -----------------------------------------      
   
   def today_attendence_fx(self):
      name_list = ['AAKIB SAIFI', 'AARAV TYAGI', 'AAYUSHI SAINI', 'ABHAY PRATAP', 'ABHINAV', 'ABHINAV SHARMA', 'ABHISHEK', 'ABHISHEK KUMAR', 'ABUBHAV MALIK', 'ADITYA GOUR', 'ADITYA KUMAR', 'ADITYA SHARMA', 'ADITYA SINGH', 'AFFAN', 'AJAJ SHAKIB', 'AKSHAY', 'AKSHAY CHAUDHARY', 'AKSHITA KHATIYAN', 'AMAN KUMAR', 'AMAN TOMAR', 'AMIT SIGH BHATI', 'ANJALI MALIK', 'ANKUSH BALIYAN', 'ANSH ARORA', 'ANSH CHAUHAN', 'ANSH SINGH', 'ANSHIKA', 'ANSHUL', 'ANUJ KUMAR', 'ANUPRIYA PAL', 'ANURAG', 'ANUSHKA GROVER', 'APOORVA MAHESHWARI', 'ARCHIT BALIYAN', 'ARCHIT TYAGI', 'ARJUN', 'ARPIT GOVIL', 'ARSH E ALAM', 'ARYAN BHATT', 'ARYAN GILL', 'ARYAN TOMAR', 'ATUL CHAUHAN', 'ATUL SHARMA', 'AYUSH', 'AYUSH GARG', 'AYUSH PAL', 'AZAD', 'AZEEM KHAN', 'BANTI SAINI', 'BHAVIKA', 'CHETAN PUNYANI', 'CHETAN SINGH', 'DAVESH SINGHAL', 'DEEPANSHI PUNDIR', 'DEV RAHI', 'DEV SHARMA', 'DEV SHARMA', 'DEV SIROHI', 'DEVANG KUMAR', 'DEVANSH DHAKA', 'DEVES GOEL', 'NISHA', 'SAKSHI', 'SAKSHI VERMA', 'SALONI', 'GAURAV BALIYAN', '-GB', 'HARSH KUMAR', 'HARSH KUMAR', 'HARSH YADAV', 'HARSHIT AHUJA', 'HARSHIT KUAMR SINGH', 'HARSHIT RANA', 'HARSHIT TYAGI', 'HIMANSHI PAL', 'HIMANSHU', 'HIMANSHU GUPTA', 'HIMANSHU KUMAR JHA', 'IFTIKAR ALAM LASKAR', 'ITIKA RASTOGI', 'IZHARAULHAQ', 'JAVED', 'JEET SAXENA', 'KAPIL', 'KARTIK KUMAR', 'KARTIK THAPA', 'KASHIF', 'KHUSHI CHAUDHARY', 'KRISH KARDAM', 'KULDEEP SAHU', 'KUNAL', 'KUNAL MEENA', 'LAKSHAY GIRI', 'LAKSHAY KASHYAP', 'LALIT CHAUDHARY', 'LAVI SHARMA', 'LOVENESH KUMAR PILANIYA', 'MANISH JAWLA', 'MANISHA SHARMA', 'MANPREET SINGH RATHI', 'MANSI', 'MANSI CHAUHAN', 'MANSI DEVI', 'MARTUNJYA RAJVANSH', 'MAYANK PANWAR', 'MEHRAJ ALAM', 'MIMANSHA SINGH', 'MOHD ALBAB RIZVI', 'MOHD ARMAN', 'MOHD KAIF', 'MOHD SAIME', 'MOHD ZAID SHAHID', 'MOHD ZAKI', 'MOHIT KHETWAL', 'MOHIT KUMAR', 'MOHIT PRAJAPATI', 'NAMAN DAGAR', 'NANDINI VERMA', 'NEHA', 'NEHA CHAUDHARY', 'NIDHI PAL', 'NIKHIL CHAUHAN', 'DHRUV', 'NISHANT', 'NISHANT NAGAR', 'ZAID KHAN', 'PRANAV BIDHUDI', 'PRASHANT LAMBA', 'PREET SHARMA', 'PRINCE KASANA', 'PRIYANSHI', 'PRIYANSHU RANA', 'PRIYANSHU VERMA', 'RAHUL BATHLA', 'RAJ TOMAR', 'RAJAT AGARWAL', 'ROHIT KUMAR', 'SACHI RASTOGI', 'SADAF KHAN', 'SAGAR PUNDIR', 'SAKSHI', 'DIPANSHU DUA', 'DIVYANSH AGGARWAL', 'GAGAN DESHWAR', 'SAMARTH GOEL', 'SAMRAT TANWAR', 'SANIYA', 'SANYAM PRATAP SINGH', 'SHADAN', 'SHASWAT MALIK', 'SHIVAM', 'SHIVANSHU', 'SHRISTI SINGH', 'SHUAIB', 'SIDDHANT', 'SONU', 'SUDHANSHI', 'SUDHANSHU TYAGI', 'SUMIT KUMAR', 'SUNNY KAUSHIK', 'SYED FAHAD ALI', 'TANISHA GUPTA', 'TANU RANA', 'TANUSH DESHWAL', 'TARANG RASTOGI', 'TARUN SINGH', 'TEJAWANI RAJPUT', 'TUSHAR KHAGWAL', 'UDAY RANA', 'UDIT CHAUHAN', 'UMANG', 'UTKARSH RAWAT', 'VAIBHAV SINGH', 'VANSH SHARMA', 'VANSHU RAJPUT', 'VARUN KUMAR', 'VASU SHARMA', 'VIDHYANSH RANA', 'VIDUSHI RANAN', 'VIKAS YADAV', 'VINEET GUPTA', 'VIPUL ARYA', 'VISHAL', 'VISHAL DESHWAL', 'WILSON NOHWAR', 'YASH KUMAR', 'YASH KUMAR', 'YASH TYAGI', 'YOGENDRA SINGH', 'YOGESH KUMAR SAINI', 'YUGDEEP SINGH', 'ZAID KHAN', 'NUPUR SOAM', 'ZOHA']
      attendence_database = {}
      # we take only 5 students for testing
      name_list_a = name_list[:5] # [:65]
      name_list_b = name_list[65:131]
      name_list_c = name_list[131:]
      sec = self.sec_options.get()
      
      # sections A, B, C
      if sec == 'Sec A':
         attendence_list = name_list_a
      elif sec == 'Sec B':
         attendence_list = name_list_b
      else:
         attendence_list = name_list_c
        
      # taking attendence
      for i in range(len(attendence_list)):
            a = tk.messagebox.askyesno(f'Student {i+1}/{len(attendence_list)}', attendence_list[i].title())
            if a is None:
               if messagebox.askyesno('!!!', 'Do you want to save \nthese student\'s attendence?') == True:
                  break
               else:
                  return 0
            attendence_database[attendence_list[i]] = a
      
      # print output list
      _student = "STUDENTS NAME"
      _status = "STATUS"
      print_at = tk.Text(root, height=15, width=40)
      print_at.insert(tk.END, f"{_student: ^23}{_status: ^10}\n\n")
      print_at.grid(padx = 10, pady=15)
      print_at.place(x=30, y=700)
      
      total_students = len(attendence_database)
      present_students = 0
      absent_students = 0
      
      # print attendence
      for i in range(len(attendence_database)):
         name_var = attendence_list[i]
         status_var = attendence_database[attendence_list[i]]
         if status_var == 1:
            status_string = 'Present'
            present_students += 1
         elif status_var == 0:
            status_string = 'Absent'
            absent_students += 1
         else:
            status_string = '------'
         print_at.insert(tk.END, f" {i+1: ^2} {name_var: ^20} : {status_string: <10}\n")
      print_at.config(state=DISABLED)
      
      # total students label
      total_students_label = tk.Label(root,
                text=f"Total Students\t: {total_students}")
      total_students_label.place(x=50, y=400)

      # present students label
      present_students_label = tk.Label(root,
                text=f"Present Students      : {present_students}")
      present_students_label.place(x=50, y=450)
      
      # absent students label
      absent_students_label = tk.Label(root,
                text=f"Absent Students       : {absent_students}")
      absent_students_label.place(x=50, y=500)
      
      # enter student name: entry
      enter_name_entry = tk.Entry(root,
               placeholder = 'Enter name',
               width = 20,
               borderwidth = 15,
               relief = tk.FLAT)
      enter_name_entry.place(x=30, y=600)
      
      # function of 'check status' button
      def check_status_fx():
         name = enter_name_entry.get().upper().strip()
         try:
            if name == "":
               messagebox.showwarning('Invalid', 'Enter name first')
            elif name in attendence_list:
               if attendence_database[name] == 1:
                  messagebox.showinfo('...', f"{name.title()}\nStatus: Present")
               else:
                  messagebox.showinfo('...', f"{name.title()}\nStatus: Absent")
            else:
               messagebox.showinfo('Not Found', f"{name.title()} not found")
         except:
            messagebox.showerror('', 'Something went wrong\nTry again')
      
      # search student status: button 
      check_status_btn = tk.Button(root,
               text = 'Check Status',
               width = 10,
               borderwidth = 4,
               relief = tk.FLAT,
               bg = 'grey',
               fg = 'white',
               command = check_status_fx
               )
      check_status_btn.place(x=430, y=600)
      
      
      


if __name__ == "__main__":
   AttendenceApp()
   
   

