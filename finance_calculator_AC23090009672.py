#Finance calcuator for bonds an investments based on user input values
import math

type_of_calculator = input(
    """ 
    Investment  - to calculate the amount of interest you'll earn on your investment
    Bond        - to calculate the amount you'll have to pay on a home loan
        
        Enter either 'investment' or 'bond' from the menu above to proceed: 
        """).lower()

#Calculates the simple or compound interest of an investment based on amount, interest rate and term.
if type_of_calculator == 'investment':
    amount_of_money = float(input("How much money are you depositing?: "))
    interest_rate = float(input("What is the interest rate as a percentage?: "))
    term = float(input("How many years do you plan on investing?: "))
    interest = input("Do you want 'simple' or 'compound' interest?: ")
    interest = interest.lower()

    if interest == 'simple':
        interest = amount_of_money * (1 + (interest_rate / 100) * term)
        interest = str(round(interest, 2))
        print(f"You'll have a total of {interest} at the end of your term")
    
    elif interest == 'compound':
        interest = amount_of_money * math.pow \
                            ((1+ (interest_rate / 100)), term)
        interest = str(round(interest, 2))
        print(f"You'll have a total of {interest} at the end of your term")

    else:
        print("The input is not valid. Please, enter 'simple' or 'compound'")

#Calculates the montly cost of a bond repayment based on house value, interest rate and term.
elif type_of_calculator == 'bond':
    house_value = float(input("What is the present value of the house?: "))
    interest_rate = float(input("What is the interest rate as a percentage?: "))
    term = int(input("How many months will your repayment plan take?: "))
    bond_repayment = ((interest_rate / 100 / 12) * house_value) \
                    / (1 - (1 + (interest_rate / 100 / 12))** (- term))
    bond_repayment = str(round(bond_repayment, 2))
    print(f"Your bond repayment will be of {bond_repayment} each month")

else:
    print("The input is not valid. Please, enter 'investment' or 'bond'")