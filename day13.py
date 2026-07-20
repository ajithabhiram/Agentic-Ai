'''
sales = int(input("Enter the sales: "))
if sales > 1000:
    print("Best Seller")
else:
    print("No Output")
'''

'''
Nested Condition -->One condition inside another-->if,else

'''

#usecase: ATM Withdrawl scnraio
#Check Wheather Card is Valid/not-->Entered pin is correct or not-->Check balance
#-->Withdrawl
'''
card_status = input("is the card valid:")
entered_pin = int(input("enter your pin:"))
correct_pin = 1234
balance = 5000
if card_status == "yes":
    if entered_pin == correct_pin:
        amount = int(input("enter withdrawal amount:"))
        if amount <= balance:
            print("withdrawal done")
            print("remaining Balance:", balance - amount)
        else:
            print("insufficient balance")
    else:
        print("incorrect pin")
else:
    print("invalid Card")

'''

#you try own sceraio foe 3 question in nested--<saketh@codegnan.com


#sample input 12000
#output plan: Trip
#input 5000
#output plan: Movie and dinner
print("================= Weekend Budget Planner =================")
budget_planner = int(input("Enter the budget planning for the Weekend: "))
if budget_planner < 0:
    print("Please don't enter negative values")
elif budget_planner > 10000:
    print("Plan: Trip")
elif budget_planner > 5000:
    print("Plan: Resort Stay")
elif budget_planner > 3000:
    print("plan: ovie and Dinner")
elif budget_planner > 1000:
    print("plan: cafe and shopping")
elif budget_planner > 500:
    print("Plan: street food and park visit")
else:
    print("Plan: stay Home")


