# Remove all
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    """
    # while e in L:
    #     L.remove(e)
    for c in L[:]:
        if c == e:
            L.remove(e)
    # second solution
    # Lcopy = L[:]
    # L.clear()
    # for c in Lcopy:
    #     if c != e:
    #         L.append(c)

L = [1,2,2,2]
remove_all(L, 2)
print(L)

L = [1,2,2,2]
remove_all(L, 1)
print(L)

L = [1,2,2,2]
remove_all(L, 0)
print(L)
print()

# Finger Exercise
def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here
    if len(Lin) <= k:
        Lin.clear()
        return
    for _ in range(k):
        del Lin[0]
    Lin.sort()  

# Examples:
L = [1,6,3]
print(id(L))
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]
print(id(L))
print()

L = [2,4,6,1,90,0,4,10]
print(id(L))
remove_and_sort(L, 9)
print(L)
print(id(L))