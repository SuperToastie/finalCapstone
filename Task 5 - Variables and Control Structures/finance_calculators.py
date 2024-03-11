"""finance_calculator"""
import math

# Ask the user to choose between an investment or bond calculator
# Choose either 'investment' or 'bond' to proceed
print("Please choose from the following calculations:\n")
print("\tINVESTMENT - to calculate the amount of interest you'll earn on your investment\n")
print("\tBOND - to calculate the amount you'll have to pay on a home loan\n")
user_choice = ""

# Check the user choice for errors. if error re-prompt.
while user_choice not in ['investment', 'bond']:
    user_choice = input(
      "Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
    if user_choice in ['investment', 'bond']:
        break # Exit the loop if the input is valid
    else:
        print("\nInvalid choice. To continue:")

# If choice is "investment", ask the user for inputs
if user_choice == "investment":
    input_not_complete = True
    while input_not_complete:
        try:
            # Deposit amount
            P = float(input("\nEnter the amount of money that you are depositing:\n"))
            # Interest rate (as a percentage)
            r = float(input("\nEnter the interest rate (e.g. 2.5):\n"))
            # Number of years they plan on investing
            t = float(input("\nEnter the number of years you plan on investing:\n"))
            input_not_complete = False
        except ValueError:
            #This code will execute if a Value Error occurs
            print("\nInvalid choice, try again:")

    interest_choice = ""
    # Check the user choice for errors. if error re-prompt.
    while interest_choice not in ['simple', 'compound']:
        interest_choice = input(
        "\nEnter 'simple' or 'compound' for the interest type:\n").lower()
        if interest_choice in ['simple', 'compound']:
            break # Exit the loop if the input is valid
        else:
            print("\nInvalid choice. To continue:")

    # Convert the interest rate to a decimal
    r = r / 100

    # Calculate & display the final amount & interest earned based on chosen type
    if interest_choice == "simple":
        # Simple interest formula: A = P * (1 + r * t)
        A = P * (1 + r * t)
        simple = A - P
        print(f"\nThe final amount is: \t{A:.2f}")
        print(f"The simple interest is: \t{simple:.2f}\n")
    elif interest_choice == "compound":
        # Compound interest formula: A = P * (1 + r) ** t
        A = P * math.pow((1+r),t)
        compound = A - P
        print(f"\nThe final amount is: \t{A:.2f}")
        print(f"The compound interest is: \t{compound:.2f}\n")

# If choice is "bond", ask the user for inputs
if user_choice == "bond":
    input_not_complete = True
    while input_not_complete:
        try:
            # Present value of the house
            P = float(input("\nEnter the present value of the house:\n"))
            # Interest rate (as a percentage)
            r = float(input("\nEnter the interest rate (as a percentage e.g 2.5):\n"))
            # Number of months they plan to take to repay the bond
            n = int(input("\nEnter the number of months you plan to take to repay the bond:\n"))
            input_not_complete = False
        except ValueError:
            #This code will execute if a Value Error occurs
            print("\nInvalid choice, try again:")

    # Calculate and display the monthly repayment
    # Monthly interest rate: i = r / 100 / 12
    i = r / 100 / 12
    # Monthly repayment formula: repayment = (i * P) / (1 - (1 + i) ** (-n))
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(f"\nThe monthly repayment is: \t{repayment:.2f}\n")
