import time
import random

# Taking user name
name = input('Enter your name: ')
name = name.capitalize()
print("Hello, " + name)
print("\n  Welcome, \n  " + name + " now you order your favorite Cold Drink.\n")

# Print input instructions
time.sleep(1)
print("Enter 1 for MAAJA, 2 for Limca and soon.")

#all lists that used in whole program
# std_price
cdtyp = ['Maaja','Limca', 'Slice',  'Thumbs up', 'Fanta', 'Mountain Dew', 'Sprite', 'Mirinda', 'Pepsi', '7up', 'Frooti']

cdcapa = ['100ml', '250ml', '500ml', '1.25 ltr', '2.25 ltr']

# print Cold drink list
i = 1
for x in cdtyp:
   print(str(i)+"--> "+x)
   i += 1
   time.sleep(0.2)

# Taking user's favorite cold drink
cdtypin = input('\nEnter Number here: ')

#check right input of user_fav_cd
while(int(cdtypin) <= 0 or int(cdtypin) >= 12):
   cdtypin = input('Please Enter a number as show in upper list: ')


# assign the value of cdtype user fav cd

    # Dictionary 
cdTypValueAssign = {"1":["Maaja", 60], "2":["Limca", 75], "3":["Slice", 53], "4":["Thumbs up", 65], "5":["Fanta", 62], "6": ["Mountain Dew", 70]}

cdtyp_value_assign = "Maaja"
std_price = 60
if cdtypin == '1':
   cdtyp_value_assign = 'Maaja'
   std_price = 60
elif cdtypin == '2':
   cdtyp_value_assign = 'Limca'
   std_price = 55
elif cdtypin == '3':
   cdtyp_value_assign = 'Slice'
   std_price = 53
elif cdtypin == '4':
   cdtyp_value_assign = 'Thumbs up'
   std_price = 65
elif cdtypin == '5':
   cdtyp_value_assign = 'Fanta'
   std_price = 62
elif cdtypin == '6':
   cdtyp_value_assign = 'Mountain Dew'
   std_price = 70
elif cdtypin == '7':
   cdtyp_value_assign = 'Sprite'
   std_price = 57
elif cdtypin == '8':
   cdtyp_value_assign = 'Mirinda'
   std_price = 56
elif cdtypin == '9':
   cdtyp_value_assign = 'Pepsi'
   std_price = 58
elif cdtypin == '10':
   cdtyp_value_assign = '7up'
   std_price = 60
else:
   cdtyp_value_assign = 'Frooti'
   std_price = 65


print("\n\nNow you can choose Quantity of " + cdtyp_value_assign)
time.sleep(1.45)

# show the cold drink capacity
j = 1
for y in cdcapa:
   print(str(j) + "--> " + y)
   j += 1
   time.sleep(0.2)

cdcapain = 1
cdcapain = input('Enter 1 for 100ml, 2 for 250ml and soon...\nEnter number here: ')

# check bottle quantity input
while(int(cdcapain) <= 0 or int(cdcapain) >= 6):
   cdcapain = input('Please Enter a number as show in upper list: ')

# quantity(ml), cdcapa_value_assign, qun_price, 
cdcapacity = {
"1":["ml", 100, 3.5],
"2":["ml", 250, 2.12],
"3":["ml", 500, 1.32], 
"4":["ltr", 1.25, 1], 
"5":["ltr", 2.25, 1/2]
}

# taking no of bottles 
numofbottles = int(input("\n\n" + name + " you can order upto 100 bottles of " + str(cdcapacity[cdcapain][1]) + str(cdcapacity[cdcapain][0]) + " of " + cdtyp_value_assign + ": "))

#check numofbottles input
while(int(numofbottles) < 1 or int(numofbottles) > 100):
   numofbottles = input('You can order upto 100 bottles only, not ' + numofbottles + ": ")

# set final price
mrp = (std_price / cdcapacity[cdcapain][2]) * numofbottles

print("We creating your bill...")
time.sleep(1.3)


# Taking BILL UI
#noOfBottle


# BILL UI
print(50*'-')
print("|\n|\tAmount          --->\t₹" + str(round(mrp, 2)) + "/-")
print("|")

print(50*'-')







