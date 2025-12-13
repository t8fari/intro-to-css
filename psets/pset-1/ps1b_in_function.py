def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	    amount_saved = (1+monthly_r)*amount_saved
	    # add portion of monthly salary saved
	    amount_saved += (portion_saved * monthly_salary)
	    months += 1
	    # yearly_salary increases by SAR at the end of every 6 months
	    if not months%6:
	        yearly_salary = (1+semi_annual_raise)*yearly_salary
	        monthly_salary = yearly_salary/12
	
	print("Number of months:", months)
	return months