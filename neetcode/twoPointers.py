# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s:str) -> bool:
    lowecasedS = s.strip().lower()
    modifiedS = ''.join(filter(str.isalnum, lowecasedS))
    i = 0
    j = len(modifiedS) - 1
    while i < j:
        if modifiedS[i] != modifiedS[j]:
            return False
        i += 1
        j -= 1
    return True
print(isPalindrome('abccba'))

# Verse 2: check alphanumeric and lower case as we go
# write our own alphanumeric function
def isPalindrome2(s:str) -> bool:
    def alphaNumeric(c):
        return ((ord('A') <= ord(c) <=ord('Z'))
            or (ord('a') <= ord(c) <= ord('z'))
            or (ord('0') <= ord(c) <= ord('9')))

    l = 0
    r = len(s) - 1
    while l < r:
        while (l < r) and (not alphaNumeric(s[l]) or not alphaNumeric(s[r])):
            if not alphaNumeric(s[l]):
                l += 1
            elif not alphaNumeric(s[r]):
                r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
print(isPalindrome2('abccba'))

