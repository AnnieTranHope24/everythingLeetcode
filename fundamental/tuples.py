# Tuples are like arrays but immutable
tup = (1, 2, 3)
print('tup = (1, 2, 3) is: ', tup)
print('tup[0] is: ', tup[0])
print('tup[-1] is: ', tup[-1])

# Can't modify, this won't work
# tup[0] = 5 throws error

# Can be used as key for HashMap/Set
myMap = {(1, 2): 'first'}
print('myMap[(1,2)] is: ', myMap[(1,2)])

mySet = set()
mySet.add((1, 2))
print('Is (1, 2) in mySet?', (1, 2) in mySet)

# Tuples can be keys but lists cannot
# myMap[[1, 2]] = "second" will throw error
