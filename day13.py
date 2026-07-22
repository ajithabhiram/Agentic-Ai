print("========== Day 13 Practice Programs ==========")
print("1. ATM Withdrawal System")
print("2. Scholarship Eligibility")
print("3. Weekend Budget Planner")
print("4. Online Shopping Discount")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("\n========== ATM Withdrawal System ==========")

    card_status = input("Is your card valid (yes/no): ").lower()

    if card_status == "yes":
        entered_pin = int(input("Enter your PIN: "))
        correct_pin = 1234
        balance = 10000

        if entered_pin == correct_pin:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                print("Withdrawal Successful")
                print("Remaining Balance:", balance - amount)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")
    else:
        print("Invalid Card")


elif choice == 2:
    print("\n========== Scholarship Eligibility ==========")

    marks = int(input("Enter your marks: "))

    if marks >= 75:
        income = int(input("Enter your annual family income: "))

        if income <= 300000:
            print("Congratulations! You are eligible for the scholarship.")
        else:
            print("Not eligible because income exceeds the limit.")
    else:
        print("Not eligible because marks are below 75.")


elif choice == 3:
    print("\n========== Weekend Budget Planner ==========")

    budget = int(input("Enter your weekend budget: "))

    if budget < 0:
        print("Please don't enter negative values.")
    elif budget > 10000:
        print("Plan: Trip")
    elif budget > 5000:
        print("Plan: Resort Stay")
    elif budget > 3000:
        print("Plan: Movie and Dinner")
    elif budget > 1000:
        print("Plan: Cafe and Shopping")
    elif budget > 500:
        print("Plan: Street Food and Park Visit")
    else:
        print("Plan: Stay Home")


elif choice == 4:
    print("\n========== Online Shopping Discount ==========")

    member = input("Are you a premium member? (yes/no): ").lower()

    if member == "yes":
        amount = int(input("Enter purchase amount: "))

        if amount >= 5000:
            print("Congratulations! You got a 20% discount.")
        else:
            print("Congratulations! You got a 10% discount.")
    else:
        print("No premium discount available.")


else:
    print("Invalid Choice! Please enter a number between 1 and 4.")
