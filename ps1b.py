# House Hunting Part B: Saving, with a raise
# !!!

MONTHS_IN_A_YEAR = 12

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04 # annual return on investment

monthly_salary = annual_salary/MONTHS_IN_A_YEAR

down_payment = total_cost * portion_down_payment

months = 0

while current_savings < down_payment:
    monthly_saved = monthly_salary * portion_saved
    additional_savings = current_savings * r/MONTHS_IN_A_YEAR
    current_savings = current_savings + monthly_saved + additional_savings
    months+=1

    if months%6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)

print("Number of months: " + str(months))
