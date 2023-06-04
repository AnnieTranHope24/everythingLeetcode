class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables aka fields
        self.nums = nums
        self.size = len(nums)

    # Functions
    # self keyword required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return self.getLength() * 2

myObj = MyClass([1, 2, 4])
print('Calling getLength we have: ', myObj.getLength())
print('Calling getDoubleLength we have: ', myObj.getDoubleLength())