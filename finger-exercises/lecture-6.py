# Bisection Search
# Find the square root of a number
x = float(input('Enter a number: '))
epsilon = 0.01
num_guesses = 1
# if 0<x<1:
#     low = x
#     high = 1
# else:
#     low = 1
#     high = x
low, high = 0, x+1
g = (low + high) / 2
while abs(g**2 - x) >= epsilon:
    if g**2 < x:
        low = g
    else:
        high = g
    g = (low + high) / 2
    num_guesses += 1

# print(f"low={low} high={high} guess={g}")
print('num_guesses =', num_guesses)
print(g, 'is close to the square root of', x)
print()


# Find the cube root of a number
n = 54321
epsilon = 0.01
num_guesses = 1
low = 0
high = n if n > 1 else 1
g = (low + high) / 2

while abs(g**3 - n) >= epsilon:
    if g**3 < n:
        low = g
    else:
        high = g
    g = (low + high) / 2
    num_guesses += 1

print('num_guesses =', num_guesses)
print(g, 'is close to the cube root of', n)
print()

# Newton-Raphson [can only be used for square root]
# Find the square root of a polynomial in one variable
print('Newton-Raphson')
n = 54321
epsilon = 0.01
num_guesses = 1
g = n/2
while abs(g*g - n) >= epsilon:
    g = g - (((g**2) - n) / (2*g))
    num_guesses += 1

print('num_guesses =', num_guesses)
print(g, 'is close to the square root of', n)
print()

# Finger exercise
# Guess N
N = 7
num_guesses = 1
low = 0
high = 1001
guess = (low + high) // 2
while guess != N:
    print('count:',num_guesses, end=', ')
    print('guess:', guess)
    num_guesses += 1
    if guess < N:
        low = guess
    else:
        high = guess
    guess = (low + high) // 2

print('Number of guesses:', num_guesses)
print('N is', N)
