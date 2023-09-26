# This code will also import the sys package.
# This package will allow the programmer more control over the code.
import sys

# This first part of the code will ask the user for inputs.
# The inputs will be used to calculate elasticities in ECO 2030.

print("Before running this program, you will have to calculate the percentage changes on paper. \n")
proceed = int(input("Would you like to continue with this program? 0 for Yes, 1 for No: "))
if proceed == 1:
    print("The program will terminate. Have a good day!")
    sys.exit()
else:
    print("The program will begin its execution. \n")

option = int(input("Would you like to calculate specific elasticities? 0 for Yes, 1 for No: "))
if option == 1:
    print("This program will not run anymore until you want to calculate elasticities.")
    sys.exit()
else:
    print("We will follow to the next step. \n")

# The next statements will explain elasticity to the user.
# This will give the user context to the program.
print("Elasticity is a measure of the responsiveness to a change in a market condition.")
print("Elasticity applies to demand and supply.")
print("It measures responses to changes in prices of goods, prices of related goods, and income. \n")

# The next code will ask for the user to input percent changes as decimals.
price_change = int(input("Enter the percent change of price for the same good in decimal form (Enter 0 for N/A): "))
if price_change != 0:
    print("This satisfies the program. \n")
else:
    print("We will not worry about price elasticity of demand then. \n")

goodB_change = int(input("Enter the percent change of price for goodB in an integer (%) form (Enter 0 for N/A): "))
if goodB_change != 0:
    print("This satisfies the program. \n")
else:
    print("We will not worry about cross-price elasticity of demand then. \n")

quantity_change = int(input("Enter the percent change of quantity in an integer (%) form (Enter 0 for N/A): "))
if quantity_change != 0:
    print("This satisfies the program. \n")
else:
    print("This program will not run anymore until you input a quantity. \n")
    sys.exit()

income_change = int(input("Enter the percent change of income in an integer (%) form (Enter 0 for N/A): "))
if income_change != 0:
    print("This satisfies the program. \n")
else:
    print("We will not worry about income elasticity of demand then. \n")

# The next section of the program will use the elasticities as conditionals.
# If quantity is 0, the entire program will terminate.
# With the proper parameters, the program will then work properly.
if price_change != 0:
    result_PED = round(quantity_change / price_change, 2)
    print("Our price elasticity of demand is: ", result_PED, "\n")
else:
    print("We are not calculating price elasticity of demand. \n")

if goodB_change != 0:
    result_CPED = round(quantity_change / goodB_change, 2)
    print("Our cross-price elasticity of demand is: ", result_CPED, "\n")
else:
    print("We are not calculating cross-price elasticity of demand. \n")

if income_change != 0:
    result_IED = round(quantity_change / income_change, 2)
    print("Our income elasticity of demand is:", result_IED, "\n")
else:
    print("We are not calculating income elasticity of demand. \n")

# The last lines of code will ask for the class name and then say goodbye for
class_str = str(input("What class is this? "))
print("We have finished a round of this program. Thank you for listening and enjoying,", class_str, "\n")
print("The program has finished its purpose.")
sys.exit()
