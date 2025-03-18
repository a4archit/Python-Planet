import time

# KBC

uname = input("Enter your name: ")
time.sleep(0.5)

welcome = f"\n\nHello {uname.title()} we hope you feel nice today. There are some important points for this program: \n\n1. We give a set of 5 questions 'one-by-one'.\n2. Each question have 4 options in which only one option will be true and rest of all will false.\n3. You will enter only option number as answer.\n4. If you give right answer then your amount will increase 10 times, if your answer wrong then your amount will less by 30%\n\n"

print(welcome)

  
# taking user permission
permission = input("Do you ready for this auspicious opportunity(Yes/No): ")
#permission.lower()


permission_list_yes = ["okay", "ok", "yes", "y", "yah", "done"] #all possibility for starting
permission_list_no = ["no", "never", "not", "nothing"] # all possibility for not start
permission_list = permission_list_yes + permission_list_no

# checking the entered value is right  or wrong
while(permission.strip() not in permission_list):
   permission = input("Enter only Yes or No: ")


# All questions, mcqs and answers dictionary
ques = {"q1":["who Invented the 3d printer","nick holonoyak","elias howe","chuck hull","christiaan huygens","chuck hull"], 
"q2":["what is the max no. of members in lok sabha", "512","542","552","532","552"],
"q3":["which veda depicts the information about the most ancient vedic age culture","Arthaveda", "samveda", "rig veda", "yajurveda", "rig veda"],
"q4":["the maginot line exists between which country", "france & germany", "germany & poland", "namibia & angola", "usa & canada","france & germany"],
"q5":["the grand canyon located in which country", "ghana", "us", "canada", "bolivia", "us"]}

global uscore
uscore = 0

permission.lower()
if(permission.strip() in permission_list_yes ):# main code block
   # main loop for all questions
   for i in range(len(ques)):
      qno = f"q{i+1}"
      print(f"\n\nQuestion {i+1}".center(50))
      time.sleep(.5)
      print(ques[qno][0].capitalize(), end="?\n")
      time.sleep(.5)
      
      # prints all MCQs
      for i in range(4):
         print(f"\tOption {i+1}: {ques[qno][i+1]}")
         time.sleep(.2)
      
      time.sleep(1)
      
      try:
         uans = int(input("Enter your answer(1-4): "))
         while(uans > 4 or uans < 1):
            uans = int(input(f"{uans} is not in option list.\nEnter a right option(1,2,3,4): "))
      except ValueError:
         print("You don't give 1,2,3 or 4 so that your score is '0' in this question.")
        # uscore-=1000 if uscore==0 else uscore == (uscore/10)
      
      if(ques[qno][uans] == ques[qno][-1]):
         print("This is right answer")
         if (uscore == 0):
            uscore += 1000
         else:
            uscore *= 10
      else:
         print("wrong answer")
         if(uscore == 0):
            print("\nWarning: Be carefull!")
         else:
            uscore = uscore-((30*uscore)/100)
      print(f"----> Score: {uscore}")
      
      
# when user not give permission then this block will execute
elif(permission.strip() in permission_list_no):
   print(f"Okay {uname.title()} we will start this game next time.")
else:
   print("Something went wrong. Please restart the program")
   



