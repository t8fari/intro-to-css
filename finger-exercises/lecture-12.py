# List comprehensions
print([e**2 for e in range(6)])
print([e**2 for e in range(6) if not e%2])

# Bisection Search
def bisection_root(x, epsilon=0.01):
    low = 0
    high = x if x>1 else 1
    mid = (low + high) /2
    while abs(mid**2 - x) >= epsilon:
        if mid**2 > x:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid

print(bisection_root(2))
print(bisection_root(2, 0.0000000000001))
print(bisection_root(512))
print(bisection_root(512, 0.5))
print(bisection_root(512, 7))
print(bisection_root(512, 0.000001))

# Finger Exercise
def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    return len([x for x in nums_list if x*x in nums_list])
    # return sum(x**2 in nums_list for x in nums_list)

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3
