# Converting a whole number to base 2

num = -29728959
def binary(num):
    is_neg = False
    if num < 0:
        is_neg = True
        num = abs(num)
    ans = ''
    if num == 0:
        ans = '0'
    while num > 0:
        ans = str(num%2) + ans
        num = num // 2
    if is_neg:
        ans = '-'+ans
    return ans

# print(binary(0))
# print(bin(-29728959)[:])
# print()


# Converting Fractions to base 2
# Find a power of two big enough to turn num in to a whole number
# Convert that whole number to base 2
# Divide the result by (2** that_number)
# >>> works if there is a p such that 2**p * num is a whole number
num = .1#.25#.625#.6875#.1#.375
p = 0
while (num*(2**p)) % 1 != 0:
    p += 1

x = int(num*(2**p))

print(p)
print(f'.{binary(x).zfill(p)}')
y = binary(x)
for i in range(p - len(y)):
    y = '0' + y
y = y[:-p] + '.' + y[-p:]
print(y)
print()

# binary of 31.25 => bin(31).bin(.25)
# print(binary(31))


# Root Approximation
x = int(input('Enter a number: '))
epsilon = 0.01
num_guesses = 0
guess = 0
increment = 0.00001

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    # if guess**2 > x:
    #     break
    guess += increment
    num_guesses += 1

print(num_guesses, 'number of guesses')
if abs(guess**2 - x) < epsilon:
    print(guess, 'is close to the square root of', x)
else:
    print('Failed on square root of', x)
    print('Last guess squared is', guess**2)
print()

# Print out the even-indexed characters
my_str = input('Enter a word: ')
s = ''
for i in range(len(my_str)):
    if not i%2:
        s += my_str[i]
print(s)
print(''.join(my_str[i] for i in range(0, len(my_str), 2)))
