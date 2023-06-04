# HashSet
mySet = set()
print('Test mySet.add(1) and mySet.add(2)')
mySet.add(1)
mySet.add(2)
print(mySet)
print('Current length of the set: ', len(mySet))

# Search in the set
print('Is 1 in mySet?', 1 in mySet)
print('Is 2 in mySet?', 2 in mySet)
print('Is 3 in mySet?', 3 in mySet)

print('Remove 2 from mySet')
mySet.remove(2)
print('Now is 2 in mySet?', 2 in mySet)

# Convert a list to a set
print('set([1, 2, 3]) is: ', set([1, 2, 3]))

print('{1, 2, 2} is: ', {1, 2, 2})