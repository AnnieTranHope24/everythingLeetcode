import re

# To remove all non-alphanumeric characters from a string
# Use regex
input = "Hello234world!!!"
s = input.lower()
s= re.sub('[^0-9a-z]', '', s)
print(s)

# If the regex is used more than once
# we can compile it
input = "Hello234world!!!"
s = input.lower()
pattern = re.compile('[^0-9a-z]')
s = re.sub(pattern, '', s)
print(s)
# Use join, filter and isalnum
input = "Hello234world!!!"
s = input.lower()
result = ''.join(filter(str.isalnum, s))
print(result)

# Another way to use isalnum
input = "Hello234world!!!"
s = input.lower()
result = ''.join([i for i in s if i.isalnum()])
print(result)
