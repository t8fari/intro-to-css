## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

cost = 800_000
down_payment = .25*cost
months = 36     #3*12
epsilon = 100
low = 0
high = 1
r = 0 #(low+high)/2
steps = 0

amount_saved = lambda r: initial_deposit*((1+(r/12))**months)
max_saved_amount = amount_saved(1)

if initial_deposit >= down_payment-100:
    r = 0.0
    steps = 0
else:
    while abs(amount_saved(r)-down_payment) >= epsilon:
        if int(amount_saved(r)) == int(max_saved_amount):
            # it is impossible to save within $100 of the required
            # down payment in 3 years given ID and r
            r = None
            steps = 0
            break
        elif amount_saved(r) < down_payment:
            low = r
        else:
            high = r
        r = (low+high)/2
        steps += 1
        # print(f"{steps}. {low}; {high}; {r}'=', {amount_saved(r)}")
        # if steps == 20: break
        # if amount_saved(r) > 200_000: break

print('Best savings rate:', r)
print('Steps in bisection search:', steps)