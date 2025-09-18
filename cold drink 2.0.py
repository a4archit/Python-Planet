from datetime import date
import random
import time


# Taking user name
name = input('Enter your name: ')
print("Hello, " + name)
print("\n  Welcome, \n  " + name + " now you order your favorite Cold Drink.\n")


# Print input instructions
time.sleep(1)
print("Enter 1 for MAAJA, 2 for Limca and soon.")


#all lists that used in whole program
cd_variety = ['Maaja', 'Limca', 'Slice',  'Thumbs up', 'Fanta', 'Mountain Dew', 'Sprite', 'Mirinda', 'Pepsi', '7up', 'Frooti','Appy']
cd_capacity = ['100ml', '250ml', '500ml','750ml','1 ltr', '1.25 ltr','2 ltr', '2.25 ltr']

# print Cold drink list
i = 1
for x in cd_variety:
   print(str(i)+"--> "+x)
   i += 1
   time.sleep(0.2)


# Taking user's favorite cold drink
cd_varietyin = input('\nEnter Number here: ')


#check right input of user_fav_cd
while(int(cd_varietyin) <= 0 or int(cd_varietyin) >= 13):
   cd_varietyin = input('Please Enter a number as show in upper list: ')


# assign the value of cd_varietye user fav cd
cd_variety_value_assign = "Maaja"
std_100ml_price = 15.75

if cd_varietyin == '1':
   cd_variety_value_assign = 'Maaja'
   std_100ml_price = 15.75
   
elif cd_varietyin == '2':
   cd_variety_value_assign = 'Limca'
   std_100ml_price = 12.75
   
elif cd_varietyin == '3':
   cd_variety_value_assign = 'Slice'
   std_100ml_price = 15.375
   
elif cd_varietyin == '4':
   cd_variety_value_assign = 'Thumbs up'
   std_100ml_price = 14.8125
   
elif cd_varietyin == '5':
   cd_variety_value_assign = 'Fanta'
   std_100ml_price = 14.625
   
elif cd_varietyin == '6':
   cd_variety_value_assign = 'Mountain Dew'
   std_100ml_price = 15.00
   
elif cd_varietyin == '7':
   cd_variety_value_assign = 'Sprite'
   std_100ml_price = 12.00
   
elif cd_varietyin == '8':
   cd_variety_value_assign = 'Mirinda'
   std_100ml_price = 14.25
   
elif cd_varietyin == '9':
   cd_variety_value_assign = 'Pepsi'
   std_100ml_price = 13.5
   
elif cd_varietyin == '10':
   cd_variety_value_assign = '7up'
   std_100ml_price = 13.875
   
elif cd_varietyin == '11':
   cd_variety_value_assign = 'Frooti'
   std_100ml_price = 16.125

else:
   cd_variety_value_assign = 'Appy'
   std_100ml_price = 16.5


print("\n\nNow you can choose Quantity of " + cd_variety_value_assign)
time.sleep(1.45)


# show the cold drink capacity
j = 1
for y in cd_capacity:
   print(str(j) + "--> " + y)
   j += 1
   time.sleep(0.2)

cd_capacityin = 1
cd_capacityin = input('Enter 1 for 100ml, 2 for 250ml and soon...\nEnter number here: ')


# Set 100ml price into x
x = std_100ml_price
y = x/3


# check bottle quantity input
while(int(cd_capacityin) <= 0 or int(cd_capacityin) >= 9):
   cd_capacityin = input('Please Enter a number as show in upper list: ')


# assign the value of quantity
cd_capacity_value_assign = 1.25
quantity_unit = 'ml'
std_price_eqn = 12
if cd_capacityin == '1':
   cd_capacity_value_assign = 100
   std_price_eqn = x
   
elif cd_capacityin == '2':
   cd_capacity_value_assign = 250
   std_price_eqn = 2*x
   
elif cd_capacityin == '3':
   cd_capacity_value_assign = 500
   std_price_eqn = (3*x) + y

elif cd_capacityin == '4':
   cd_capacity_value_assign = 750
   std_price_eqn = (4*x) + y
   
elif cd_capacityin == '5':
   cd_capacity_value_assign = 1
   quantity_unit = 'ltr'
   std_price_eqn = (5*x) - y
   
elif cd_capacityin == '6':
   cd_capacity_value_assign = 1.25
   quantity_unit = 'ltr'
   std_price_eqn = (5*x)
  
elif cd_capacityin == '7':
   cd_capacity_value_assign = 2
   quantity_unit = 'ltr'
   std_price_eqn = (6*x) + y
    
else:
   cd_capacity_value_assign = 2.25
   quantity_unit = 'ltr'
   std_price_eqn = (7*x) - y


# taking no of bottles 
numofbottles = int(input("\n\n" + name + " you can order upto 100 bottles of " + str(cd_capacity_value_assign) + quantity_unit + " of " + str(cd_variety_value_assign) + ": "))


#check numofbottles input
while(int(numofbottles) < 1 or int(numofbottles) > 100):
   numofbottles = input('You can order upto 100 bottles only, not ' + numofbottles + ": ")


# set final price
without_discount_mrp = std_price_eqn * numofbottles

print("We creating your bill...")
time.sleep(1.3)


# Random function
def random_number(y):
    numbers = "0123456789"
    digit = y
    rdm_num = "".join(random.sample(numbers, digit))
    return rdm_num


# Date function
def DATE(format):
    datex = date.today()
    _date_ = datex.strftime(format)
    return _date_


# Creating Random discount range 5% to 9%
num_for_discount = "56789"
rdm_num_for_discount = "".join(random.sample(num_for_discount, 1))
percentage = rdm_num_for_discount
percentage_amount = (without_discount_mrp/100)*int(percentage)
round(percentage_amount, 2)

# Taking BILL UI
cd_variety_type = cd_variety[int(cd_varietyin)-1]
cd_quantity_type = cd_capacity[int(cd_capacityin)-1]
bill_id = random_number(4)
today_date = DATE("%d/%m/%Y")
mrp = without_discount_mrp - percentage_amount
round(mrp, 2)


# BILL UI
print()
print(50*'-')
print("| NAME\t     : " + name.upper() + "\n| ID\t     : " + bill_id + "\n| ORDER DATE : " + today_date)
print("|\n|\tVariety \t   ---> " + str(cd_variety_type))
print("|\tQuantity \t   ---> " + str(cd_quantity_type))
print("|\tPrice per bottle   ---> " + str(std_price_eqn))
print("|\tBottles \t   ---> " + str(numofbottles))
print("|\n|\tAmount \t\t   --->\t₹" + str(without_discount_mrp) + "/-")
print("|\tDiscount \t   ---> " + str(percentage) + "%" + "\n|\t\t\t        -" + str(percentage_amount) + "/-")
print("|\n|\tTotal Amount \t   ---> " + str(mrp) + "/-")
print("|")

print(50*'-')







