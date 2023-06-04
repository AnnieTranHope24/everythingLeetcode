# Arrays (called lists in Python)
arr = [1, 2, 3]
print('This is an array or list: ', arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print('Array after being appended 4 and 5: ', arr)

arr.pop()
print('Array after being popped: ', arr)

arr.insert(1, 7)
print('Array after being inserted 7 to index 1: ', arr)

arr[0] = 0
arr[3] = 0
print('Array after changing the elements with indexes 0 and 3 to be 0: ', arr)
# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print('Initialize arr of size n with default value of 1: ', arr)
print('The length of the array is: ', len(arr))

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print('We have this array: ', arr)
print('And the element at index -1 is ', arr[-1])
print('And the element at index -2 is ', arr[-2])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print('We have this array: ', arr)
print('arr[1:3] is:', arr[1:3])

# Last index is non-inclusive, but no out of bounds error
print('arr[0:10] is: ', arr[0:10])

# Unpacking
a, b, c = [1, 2, 3]
print('Unpacking arr [1, 2, 3] using a, b, c = [1, 2, 3]: ', a, b, c)

# Be careful: this throws an error
# a, b = [1, 2, 3]

# Looping through arrays
nums = [1, 2, 3]

# Using index
print('Test loop using range(len(nums))')
for i in range(len(nums)):
    print(nums[i])

# Without index
print('Test loop using num in nums')
for num in nums:
    print(num)

# With index and value
print('Test loop using enumerate(nums')
for i, num in enumerate(nums):
    print(i, num)

# Loop through multiple arrays simultaneously with unpacking
print('Test looping thru multiple arrays using zip(nums1, nums2)')
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for num1, num2 in zip(nums1, nums2):
    print(num1, num2)

# Reverse
print('Test arr.reverse()')
arr = [1, 3, 5]
arr.reverse()
print(arr)

# Sorting ascending
print('Test arr.sort()')
arr = [5, 4, 7, 3 ,8]
arr.sort()
print(arr)

# Sorting descending
print('Test arr.sort(reverse = True)')
arr.sort(reverse=True)
print(arr)

# Sorting alphabetical
print('Test arr.sort() alphabetically')
arr = ['bob', 'alice', 'jane', 'joe']
arr.sort()
print(arr)

# Custome sort (by length of the string)
print('Sort arr by length using key=lambda x: len(x)')
arr.sort(key=lambda x : len(x))
print(arr)

# List Comprehension
print('List comprehension using [i for i in range(5)]')
arr = [i for i in range(5)]
print(arr)

# 2-D List
print('2-D list using [[0] * 4 for i in range(4)]')
arr = [[0] * 4 for i in range(4)]
print(arr)
arr[0][1] = 1
print('arr[0][1] is: ', arr[0][1])
print('arr[1][1] is: ', arr[1][1])


# This won't work as you expect it to
# Modify one array will modify the rest
print('Try [[0] * 4] * 4 and see it fails')
arr = [[0] * 4] * 4
print(arr)
print(arr)
arr[0][1] = 1
print('arr[0][1] is: ', arr[0][1])
print('arr[1][1] is: ', arr[1][1])

# Join two lists
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print('Join two arrs: ', arr1 + arr2)