# Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N. The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. Hint: use a loop that increments a counter—you decide when the counter should stop.
N = int(input("Enter a number: "))
found = False
for g in range(abs(N)+1):
    if g**3 == abs(N):
        found = True
    if g**3 > abs(N) or found:
        break
if not found:
    print(N, "is not a perfect cube")
else:
    if N < 0:
        g = -g
    print("Cube root of", N, "is", g)
print(g)

### second version
print("second version")
for g in range(abs(N)+1):
    if g**3 >= abs(N):
        break
if g**3 != abs(N):
    print(N, "is not a perfect cube")
else:
    if N < 0:
        g = -g
    print("Cube root of", N, "is", g)


### ticket fundraiser
print()
# a + b + c = 10
# b = a - 2
# c = 2 * a
# a, b, c = 0, 0, 0

for i in range(2, 11):
    if i+(i-2)+(2*i) == 10:
        print('Alyssa sold', i, "tickets")

n = 1000
for a in range(n+1):
    b = max(a-20, 0)
    c = a * 2
    if a + b + c == n:
        print('Alyssa sold', a, "tickets")


"""
### square root
# Guess and check algorithm
# for loop solution
x = int(input("Enter a number: "))
if x < 0:
    print(x, "is not a perfect square", "-- for solution")
for i in range(1, x):
    if i*i == x:
        print("Square root of", x, "is", i, "-- for solution")
        break
    elif (i*i) > x:
        print(x, "is not a perfect square", "-- for solution")
        break

# while loop solution
g = 1
while g*g < x:
    g += 1
if g*g == x:
    print("Square root of", x, "is", g, "-- while solution")
else:
    print(x, "is not a perfect square", "-- while solution")


# secret number game
print()
secret = 50
found = False
for i in range(1, 11):
    if i == secret:
        print("The secret number is", secret)
        found = True
if not found:
    print("I didn't find the secret number")
"""