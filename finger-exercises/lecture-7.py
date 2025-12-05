# Is i even

def is_even(i):
    """
    Check if i is even
    """
    return not i%2

# print(is_even(5))
# print(is_even(-33))
# print(is_even(1))
# print(is_even(-100))
# print(is_even(0))


def div_by(n, d):
    """
    n and d are ints > 0
    Return True if d divides n evenly
    """
    return not n%d

# print()
# print(div_by(4,2))
# print(div_by(9,2))
# print(div_by(15,3))
# print(div_by(4,10))
# print(div_by(0,3))
# print(div_by(195,13))


def sum_odds(a, b):
    """
    Add all the odd integers between a and b inclusive
    """
    # s = 0
    # for i in range(a, b+1):
    #     if i%2:
    #         s += i
    # return s
    return sum(i for i in range(a, b+1) if i%2)

# print()
# print(sum_odds(1, 5))
# print(sum_odds(2, 7))
# print()


# Finger Exercises
# Q1
def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic ax² + bx + c.
    """
    return (a*x**2) + (b*x) + c


# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3
print(eval_quadratic(1, 5, 3, 2)) # prints 17
print()

# Q2
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    e1 = eval_quadratic(a1, b1, c1, x1)
    e2 = eval_quadratic(a2, b2, c2, x2)
    print(e1 + e2)


# Examples:    
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None
