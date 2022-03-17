# House Hunting Part C: Finding the right amount to save away
# produce the portion of the salary that should be saved
# !!!

MONTHS_IN_A_YEAR = 12

annual_salary = float(input("Enter your starting annual salary: "))

semi_annual_raise = 0.07
r = 0.04 # annual return on investment
down_payment_portion = 0.25
total_cost = 1000000

steps = 0
epsilon = 100

current_savings = 0
down_payment = total_cost * down_payment_portion

low = 0
high = 10000
portion_saved = 5000

while abs(current_savings - down_payment) >= epsilon:
    current_savings = 0
    monthly_salary = annual_salary/MONTHS_IN_A_YEAR

    for months in range(36):
        monthly_saved = monthly_salary * (portion_saved / 10000)
        additional_savings = current_savings * r/MONTHS_IN_A_YEAR
        current_savings = current_savings + monthly_saved + additional_savings
        months += 1

        if months%6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    
    if high == low:
        break
    elif current_savings > down_payment:
        high = portion_saved
    else:
        low = portion_saved
    
    portion_saved = (high + low)/2
    steps += 1

if high == low:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: " + str(format(portion_saved/10000,'.4')))
    print("Steps in bisection search: " + str(steps))
