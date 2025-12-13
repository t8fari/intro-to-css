## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
monthly_salary = yearly_salary/12
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_of_dream_home
amount_saved = 0
r = 0.05
monthly_r = r/12
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < down_payment:
    # add monthly return as % of the amt saved at the start of the month
    amount_saved += (amount_saved * monthly_r)
    # add portion of monthly salary saved
    amount_saved += (portion_saved * monthly_salary)
    months += 1

print("Number of months:", months)
# print("Amount saved", amount_saved)