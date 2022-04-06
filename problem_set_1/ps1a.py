# House Hunting
# produce how long it will take to save enough money for down payment

MONTHS_IN_A_YEAR = 12

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04 # annual return on investment

monthly_salary = annual_salary/MONTHS_IN_A_YEAR

down_payment = total_cost * portion_down_payment
monthly_saved = monthly_salary * portion_saved

months = 0

while current_savings < down_payment:
    additional_savings = current_savings * r/MONTHS_IN_A_YEAR
    current_savings = current_savings + monthly_saved + additional_savings
    months+=1

print("Number of months: " + str(months))
