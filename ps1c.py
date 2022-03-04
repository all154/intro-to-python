# House Hunting Part C: Finding the right amount to save away
# produce the portion of the salary that should be saved
# !!!

MONTHS_IN_A_YEAR = 12

annual_salary = float(input("Enter your starting annual salary: "))

semi_annual_raise = 0.07
r = 0.04 # annual return on investment
down_payment_portion = 0.25
total_cost = 1000000
months = 36

portion_saved = 0.5
steps = 0

print("Best savings rate: " + str(portion_saved))
print("Steps in bisection search: " + str(steps))
