# If statements don't need parentheses or curly braces
n = 1
result = ''
if n > 2:
    result = 'n is greater than 2'
elif n == 2:
    result = 'n is 2'
else:
    result = 'n is less than 2'
print(result)

# Parentheses needed for multi-line conditions
# and = &&
# or = ||

n, m, k = False, 'Annie', 1
if (n and m == 'Annie') or k == 0:
    print('It\'s Annie or k is 0')
else:
    print('Something else')
