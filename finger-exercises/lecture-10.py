def make_ordered_list(n):
    """
    n is a positive int
    Return a list containing all ints in order from 0 to n inclusive
    """
    # return [i for i in range(n+1)]
    return list(range(n+1))


print(make_ordered_list(10))
print(make_ordered_list(0))
print(make_ordered_list(1))
print()


def remove_elem(L, e):
    """
    L is a list
    e is an object
    Return a new list with elements in the same order as L but without any elements equal to e 
    """
    return [x for x in L if x != e]


print(remove_elem([1,2,2,2], 2))
print(remove_elem([1,2,5,'cat','bat',10], '2'))
print(remove_elem([1,2,5,'cat','bat',10], 'cat'))
print(remove_elem([1,2,3,4], 5))
print(remove_elem([1,2,[3,4],[5,6],7,8], [3,4]))
print()


def count_words(sen):
    """
    sen is a string representing a sentence
    Return how many words are in s (i.e., a word is a sequence of characters between spaces)
    """
    return len(sen.split())


print(count_words("Hello it's me"))
print()


def sort_words(sen):
    """
    sen is a string representing a sentence
    Returns a list containing all the words in sen but sorted in alphabetical order
    """
    return sorted(sen.split())


print(sort_words("Hello it's me"))
print(sort_words("look at this photograph"))
print()

# L += L       --- mutates L
# L = L + L    --- creates a new list


def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    for func in Lf:
        if not func(n):
            return False
    return True

def is_odd(n):
    return n%2

def is_divisible_by_5(n):
    return not n%5

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**.5)):
        if not n%i:
            return False
    return True


print(all_true(2, [is_odd, is_divisible_by_5, is_prime]))
print(all_true(5, [is_odd, is_divisible_by_5, is_prime]))
