def bisection_root(x):
    epsilon = 0.0000001
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


# print(bisection_root(4))
# print(bisection_root(0.5))
# print(bisection_root(99))
# print(bisection_root(102))
# print(bisection_root(10))


def count_nums_with_sqrt_close_to(n, epsilon):
    """
    Returns how many integers have a square root within epsilon of n
    """
    count = 0
    for i in range((n**3)+1):
        if abs(bisection_root(i) - n) < epsilon:
            count += 1
    return count


# print(count_nums_with_sqrt_close_to(10, 0.1))
# print(count_nums_with_sqrt_close_to(10, 1))


def is_even(n):
    return not n%2


def apply(criteria, n):
    """
    Return how many ints from 0 to n (inclusive) match the criteria (i.e. return True when run with criteria)
    """
    return sum(1 for i in range(n+1) if criteria(i))


# print(apply(is_even, 10))


# Finger Exercise
def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    return len(set(s1)) == len(set(s2))


# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False