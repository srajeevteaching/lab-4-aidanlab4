# Programmers: Aidan, Nicol
# Course: CS151, Dr. Rajeev
# Date: Thu Oct 7 Lab: 4
# Program Inputs: Data plan and coupon if applies
# Program Outputs: Amount owed
# lab4fall

# Problem Write a program to determine how much a customer owes their mobile phone provider based on their
# subscription package and how much data they used. There are three different subscription packages for its customers:

# Green: 2GB of data for $49.99/month. Additional GB are $14.99/GB. Additionally, if the customer has a coupon
# (only applies to green package), there is a further discount of $20 on bills that are $75 or more.
# Orange: 4GB of data for $69.99/month. Additional GB are $9.99/GB. Purple: $99.99/month for unlimited data.
# Round: Use the round function to round your output to two decimal places.

# Do not do separate price calculations for each package: Use conditional statements to set up variables that plans
# have in common. Then do the cost calculation in one place using those variables.

# Input Validation: Your program must work regardless of the case the package name is typed in and any blank spaces
# surrounding it; i.e. " gREEn " should be recognized as valid. If the user inputs an invalid package name, tell them
# that it was invalid and do not give them a bill amount or do any calculations. Do not accept negative numbers
# for extra data used.

# input for plan
plan = input("What is your plan?")
# if chain
if plan.lower() == "green":
    data = float(input("How much data did you use?"))
    months = float(input("How many months will you use the plan?"))
    if data > 2:
        coupon = input("Do you have coupon for the Green plan(yes or no)?")
        bill = 64.98 * months
        if coupon.lower() == "yes" and bill >= 75:
            bill -= 20
            print("Your bill after ", months, " with a coupon is $%.2f" % bill, ".")
        else:
            print("Your bill after ", months, " is $%.2f" % bill, ".")
    elif 0 < data <= 2:
        bill = 49.99 * months
        print("Your bill after ", months, "months is $%.2f" % bill, ".")
elif plan.lower() == "orange":
    data = float(input("How much data did you use?"))
    months = float(input("How many months will you use the plan?"))
    if data > 4:
        bill = 79.98 * months
        print("Your bill after ", months, "months is $%.2f" % bill, ".")
    elif 0 < data <= 4:
        bill = 69.99 * months
        print("Your bill after ", months, "months is $%.2f" % bill, ".")
elif plan.lower() == "purple":
    months = float(input("How many months will you use the plan?"))
    bill = 99.99 * months
    print("Your bill after ", months, "months is $%.2f" % bill, ".")
else:
    print("Plan is invalid.")



