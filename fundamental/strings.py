# Strings are similar to arrays
s = 'abc'
print('First we have this string: ', s)

print('s[0:2] is: ', s[0:2])

# But they are immutable. This won't work
# s[0] = 'A' throws error

# This creates a new string
s += 'def'
print('s += "def" is: ', s)

# Valid numeric strings can be converted
print('int("123") + int("456") is ', int('123') + int('456'))

# Add numbers can be converted to strings
print('str("123") + str("123") is: ', str("123") + str("123"))

# Get the ASCII value of a char
print('ord("a") is', ord('a'))
print('ord("b") is', ord('b'))

# Combine a list of strings with an empty string delimitor
strings = ['ab', 'cd', 'ef']
print('"".join(strings) is ', "".join(strings))

# Test lower
s = ' 12anNie '
s.lower()
print(s.lower())