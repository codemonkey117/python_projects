print("Welcome to the budget tool! Please enter the following data to process monthly expenses.")

monthly_income = float(input('Please enter your monthly income.'))

rent_or_mortgage = float(input('Please enter your monthly expenses for rent or mortgage'))
utilities = float(input('Please enter your monthly expenses for garbage, gas and water'))
cell_phone = float(input('Please enter your cell phone bill.'))
groceries = float(input('Please enter your monthly expenses for groceries.'))
going_out = float(input('Please enter your monthly expenses for dining out and entertainment.'))
home_insurance = float(input('Please enter your monthly expenses for renter or homeowners insurance.'))
car_payment = float(input('Please enter your monthly expenses for car payments.'))
auto_insurance = float(input('Please enter your monthly expenses for auto insurance.'))
retirement = float(input('Please enter your monthly expenses for 401k retirement or Roth IRA.'))
health_insurance = float(input('Please enter your monthly expenses for health insurance'))
student_loan = float(input('Please enter monthly expenses for student loan payments.'))
emergency_fund = float(input('Please enter monthly expenses for emergency funds.'))

percentage_for_rent = (rent_or_mortgage/monthly_income)*100
percentage_for_utilities = (utilities/monthly_income)*100
percentage_for_cell_phone = (cell_phone/monthly_income)*100
percentage_for_groceries = (groceries/monthly_income)*100
percentage_for_going_out = (going_out/monthly_income)*100
percentage_for_home_insurance = (home_insurance/monthly_income)*100
percentage_for_car_payment = (car_payment/monthly_income)*100
percentage_for_auto_insurance = (auto_insurance/monthly_income)*100
percentage_for_retirement = (retirement/monthly_income)*100
percentage_for_health_insurance = (health_insurance/monthly_income)*100
percentage_for_student_loan = (student_loan/monthly_income)*100
percentage_for_emergency_fund = (emergency_fund/monthly_income)*100

print(f'Yearly income is ${monthly_income*12:.2f}')

print(f'Rent or Mortgage is {percentage_for_rent:.2f}% of ${monthly_income:.2f} @ ${rent_or_mortgage:.2f} a month, \nand ${(rent_or_mortgage*12):.2f} a year.')
print(f'Utilities are {percentage_for_utilities:.2f}% of ${monthly_income:.2f} @ ${utilities:.2f} a month, \nand ${(utilities*12):.2f} a year.')
print(f'Cell phone expenses are {percentage_for_cell_phone:.2f}% of ${monthly_income:.2f} a month, \nand ${(cell_phone*12):.2f} a year.')
print(f'Grocery expenses are {percentage_for_groceries:.2f}% of ${monthly_income:.2f} @ ${groceries:.2f}, \nand ${(groceries*12):.2f} a year.')
print(f'Going out expenses are {percentage_for_going_out:.2f}% of ${monthly_income:.2f} @ ${going_out:.2f} a month, \nand ${(going_out*12):.2f} a year.')
print(f'Home insurance expenses are {percentage_for_home_insurance:.2f}% of ${monthly_income:.2f} @ ${home_insurance:.2f} a month, \nand ${(home_insurance*12)} a year.')
print(f'Car payment expenses are {percentage_for_car_payment:.2f}% of ${monthly_income:.2f} a month @ ${car_payment:.2f} a month, \nand ${(car_payment*12):.2f} a year.')
print(f'Auto insurance expenses are {percentage_for_auto_insurance:.2f}% of ${monthly_income:.2f} a month @ ${auto_insurance:.2f} a month, \nand ${(auto_insurance*12)} a year.')
print(f'Retirement expenses are {percentage_for_retirement:.2f}% of ${monthly_income:.2f} a month @ ${retirement:.2f} a month, \nand ${(retirement*12):.2f} a year')
print(f'Health insurance expenses are {percentage_for_health_insurance:.2f}% of ${monthly_income:.2f} a month @ ${health_insurance:.2f} a month, \nand ${(health_insurance*12):.2f} a year.')
print(f'Student loan expenses are {percentage_for_student_loan:.2f}% of ${monthly_income:.2f} a month @ ${student_loan:.2f}a month,\nand ${(student_loan*12):.2f} a year.')
print(f'Emergency expenses a month are {percentage_for_emergency_fund:.2f}% of ${monthly_income:.2f} a month @ ${emergency_fund:.2f} a month,\nand{(emergency_fund*12):.2f} a year.')