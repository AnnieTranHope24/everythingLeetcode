# HashMap aka dict
myMap = {}
myMap['annie'] = 16
myMap['cham'] = 11
print('My map is: ', myMap)
print('The length of myMap is: ', len(myMap))
myMap['annie'] = 1
print('Value of myMap["annie"] after changing its value to 1 is: ', myMap['annie'])
print('Is annie in myMap? ', 'annie' in myMap)
myMap.pop('annie')
print('Is annie in myMap after doing myMap.pop("annie")?', 'annie'in myMap)

# Initialize HashMap with key and value pairs
myMap = {'thao':1999, 'tinh': 2001}
print(myMap)

# Dict comprehension
myMap = {i : 2*i for i in range(4)}
print('myMap = {i : 2*i for i in range(4)} is: ', myMap)

# Looping through maps
myMap = {'thao':1999, 'tinh': 2001}
print('Loop thru the keys')
for k in myMap.keys():
    print(k, myMap[k])

print('Loop thru the values')
for val in myMap.values():
    print(val)

print('Loop thru both keys and values using myMap.items()')
for key, value in myMap.items():
    print(key, value)

# get(key, value)
myMap = {'thao':1999, 'tinh': 2001}
print('Test the get(key, value) method')
print('myMap.get("thao") = ', myMap.get('thao'))
print('myMap.get("ngoc", 0) = ', myMap.get('ngoc', 0))
print('myMap now is ', myMap)
print('myMap["thao"] is ', myMap["thao"])