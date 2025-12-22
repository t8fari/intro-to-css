# try  except  else  finally
# raise ValueError("something is wrong")

def pairwise_div(Lnum, Ldenom):
    """
    Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    
    Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenom
    
    Raise a ZeroDivisionError if Ldenom contains 0
    """
    assert len(Lnum)==len(Ldenom), "the length of the lists must be equal"
    assert Lnum and Ldenom, "the lists must not be empty"
    assert 0 not in Ldenom, "the denominator cannot be 0"

    return [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    # try:
    #     return [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    # except ZeroDivisionError:
    #     raise ZeroDivisionError("couldn't divide by 0")
    # else:
    #     return result


L1 = [4, 5, 6]
L2 = [1, 2, 3]
# print(pairwise_div(L1, L2))

L1 = [4, 5, 6]
L2 = [1, 0, 3]
# print(pairwise_div(L1, L2))

# unequal lengths
L1 = [4, 5]
L2 = [1, 2, 3]
# print(pairwise_div(L1, L2))

# 0 in denominator
L1 = [4, 5, 6]
L2 = [1, 0, 3]
# print(pairwise_div(L1, L2))

# one empty list
L1 = []
L2 = [1, 2, 3]
# print(pairwise_div(L1, L2))

# two empty lists
L1 = []
L2 = []
# print(pairwise_div(L1, L2))


# Finger Exercise
def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    count = 0
    for x in L:
        if type(x)==str:
            count += len(x)
        elif type(x)==list:
            for j in x:
                if type(j)==str:
                    count += len(j)
                else:
                    raise ValueError("an int was found")
        else:
            raise ValueError("an int was found")
    return count

# Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError