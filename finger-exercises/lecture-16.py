# inefficient
def fib(x):
    """
    Return the nth Fibonacci number
    """
    if x==1 or x==2:
        return 1
    return fib(x-1) + fib(x-2)

print(fib(5))
print(fib(1))
print(fib(2))
print(fib(3))
# print(fib(34))
# print(fib(513))


# efficient fibonacci
def fib(n, d):
    """Return the nth Fibonacci number"""
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:1}
print(fib(6, d))
print(fib(513, d))


# Basketball score count - inefficient
def score_count(x):
    """
    Return all the ways to make a score of x by adding 1, 2 amd/or 3 together. Order doesn't matter
    """
    if x==1 or x==2 or x==3:
        return x
    return score_count(x-1) + score_count(x-2) + score_count(x-3)

print()
print(score_count(4))
print(score_count(5))
# print(score_count(34))
print()


# Basketball score count - efficient
def score_count(x, d):
    """
    Return all the ways to make a score of x by adding 1, 2 amd/or 3 together. Order doesn't matter
    """
    if x==1 or x==2 or x==3:
        return x
    elif x in d:
        return d[x]
    else:
        a = score_count(x-1, d)
        b = score_count(x-2, d)
        c = score_count(x-3, d)
        d[x-1] = a
        d[x-2] = b
        d[x-3] = c
        return a + b + c

d = {}
print()
print(score_count(4, d))
print(score_count(5, d))
print(score_count(34, d))
print()


# Sum the elements in a list
def sum_list(lst, ans=0):
    for x in lst:
        if type(x) != list:
            ans += x
        else:
            ans += sum_list(x)
    return ans

l = [1,2,[3,4,5,[6,[7,8]],[9],[[[[[10]]]]]]]
print(sum_list(l))


# Sum the lengths of all strings in L
def total_len_recur(L):
    """
    Return the total length of all strings inside L
    """
    if len(L)==1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])

test = ['ab', 'c', 'defgh']
print(total_len_recur(test))  # 8


# Check if e is in L or not
def in_list(L, e):
    # return str(e) in str(L)
    if len(L) == 1:
        return L[0] == e
    else:
        if L[0] == e:
            return True
        else:
            return in_list(L[1:], e)

print(in_list([2,1,5,8], 10))
print(in_list([2,1,5,8,10], 10))

# In-list simplified
def in_list_simplified(L, e):
    if len(L) == 0:
        return False
    elif L[0] == e:
        return True
    else:
        return in_list(L[1:], e)

print(in_list_simplified([2,1,5,8], 10))
print(in_list_simplified([2,1,5,8,10], 10))
print()


# In list of lists
def in_list_of_lists(L, e):
    if len(L) == 0:
        return False
    elif e in L[0]:
        return True
    else:
        return in_list_of_lists(L[1:], e) 

test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 0))    # False
print(in_list_of_lists(test, 3))    # True
print(in_list_of_lists([], 3))    # False
print('-----------')


# In-list without using the in operator
def in_list_(L, e):
    if len(L)==0:
        return False
    else:
        for x in L[0]:
            if x == e:
                return True
        return in_list_of_lists(L[1:], e)

test = [[1,2], [3,4], [5,6,7]]
print(in_list_(test, 0))    # False
print(in_list_(test, 3))    # True
print(in_list_([], 3))    # False


# Reverse list
def reverse_list(L):
    if len(L) == 1:
        return L
    else:
        return L[-1:] + reverse_list(L[:-1])
        # return reverse_list(L[1:]) + [L[0]]

print(reverse_list([1,2,3,4]))
print(reverse_list([1,2,'abc']))
test = [1, ['d'], ['e', ['f', 'g']]]
print(reverse_list(test))


# Reverse list - everything
def reverse(L):
    if len(L) == 0:
        return []
    elif type(L[0]) != list:
        return reverse(L[1:]) + [L[0]]
    else:
        return reverse(L[1:]) + [reverse(L[0])]

test = [1, ['d'], ['e', ['f', 'g']]]
print(reverse(test))
test = [[1,2], 3, 4, [[5,6],[7,8]]]
print(reverse(test))
print(reverse([1]))
print(reverse([[1,2],3]))
print('-----------')

# Flattern list
def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    ans = []
    for x in L:
        if type(x) != list:
            ans.append(x)
        else:
            # ans.extend(flatten(x))
            ans += flatten(x)
    return ans

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]
l = [1,2,[3,4,5,[6,[7,8]],[9],[[[[[10]]]]]]]
print(flatten(l))
