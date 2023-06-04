# Given an integer array nums,
# return true if any value appears at least twice in the array, and return false if every element is distinct
from collections import Counter


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    mySet = set(nums)
    return len(nums) != len(mySet)

print('Test containsDuplicate', containsDuplicate([1, 2, 3]))

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return Counter(s) == Counter(t)
print('Test isAnagram: ', isAnagram('abc', 'cba'))

def isAnagram2(s, t):
    if len(s) != len(t):
        return False

    arr = [0 * i for i in range(26)]
    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1
    for i in arr:
        if i != 0:
            return False
    return True
print('Test isAnagram2: ', isAnagram2('anagram', 'gramana'))

def isAnagram3(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
print('Test isAnagram3: ', isAnagram3('anagram', 'gramana'))

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

# Strategy: build as we go
def twoSum(nums, target):

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    myMap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in myMap:
            return [myMap[diff], i]
        myMap[num] = i

print('Test twoSum([3, 2, 4], 6)', twoSum([3, 2, 4], 6))
print('Test twoSum([3, 2, 4], 5)', twoSum([3, 2, 4], 5))
print('Test twoSum([3, 3], 6)', twoSum([3, 3], 6))