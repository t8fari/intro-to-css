# for loop
def mult(a, b):
    tot = 0
    for _ in range(b):
        tot += a
    return tot

# while loop
def mult(a, b):
    tot = 0
    while b > 0:
        tot += a
        b -= 1
    return tot

# recursion
def mult(a, b):
    if b==1:
        return a
    return a + mult(a, b-1)

print(mult(5,8))


def power_recur(n, p):
    if p==0:
        return 1
    return n * power_recur(n, p-1)

print(power_recur(2, 3))
print(power_recur(2, 5))


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

print(fact(0))
print(fact(4))
print(fact(5))