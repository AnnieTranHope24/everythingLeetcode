def multiply(num1, num2):
    return num1 * num2
print('multiply(2, 3) is: ', multiply(2, 3))

# Nested functions have access to outer variables
def addEverythingTo3(num1, num2):
    three = 3
    def addTwoInputToThree():
        return num1 + num2 + three
    return addTwoInputToThree()
print('addEverythingTo3(1, 2) is: ', addEverythingTo3(1, 2))

# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying arrays works
        for i in range(len(arr)):
            arr[i] *= 2

        # But val *= 2 won't work
        # unless using nonlocal

        nonlocal val
        val *= 2
    helper()
    print(arr, val)
nums = [1, 3]
val = 2
print('double([1, 3], 2) is: ')
double(nums, val)


