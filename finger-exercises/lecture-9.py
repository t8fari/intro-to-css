def is_even(n):
    return not n%2


def apply(criteria, n):
    """
    Return how many ints from 0 to n (inclusive) match the criteria (i.e. return True when run with criteria)
    """
    return sum(1 for i in range(n+1) if criteria(i))

print(apply(lambda x: not x%2, 10))
print((lambda x: x%2)(8))
print((lambda x: x%2)(5))
print((lambda x: x**2)((lambda x: x**2)(3)))


def char_count(s):
    """
    Return the number of vowels in s, and the number of consonants in s
    """
    n_vowel = sum(1 for c in s if c in 'aeiou')
    n_conso = sum(1 for c in s if c not in 'aeiou') #len(s)-n_vowels
    return n_vowel, n_conso

print(char_count('programming'))
print(char_count(''))
print(char_count(' ')) # fail


def mean(*args):
    """
    Return the mean of the numbers
    """
    tot = sum(i for i in args)
    return tot / len(args)

print(mean(1,2,3,4,5,6))
print(mean(6,0,9))


def sum_and_product(L):
    """
    Return the sum of all elements in L, and the product of all elements in L
    """
    tot = 0
    prod = 1
    for i in L:
        tot += i
        prod *= i
    return tot, prod

print(sum_and_product([1,2,3,4]))


# Finger Exercise
def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    sum_prod = 0
    for i in range(len(tA)):
        sum_prod += tA[i]*tB[i]
    return len(tA), sum_prod


# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)