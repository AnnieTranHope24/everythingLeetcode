# Given a sing s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input sing is valid.
#
# An input sing is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s) -> bool:
    arr = []
    myMap = {'(' : ')', '{' : '}', '[' : ']'}
    for c in range(len(s)):
        if s[c] == '(' or s[c] == '{' or s[c] == '[':
            arr.append(s[c])
        else:
            # arr.pop()
            if len(arr) == 0:
                return False
            else:
                if s[c] == myMap.get(arr[-1]):
                    arr.pop()
                else:
                    return False
    if len(arr) != 0:
        return False
    else:
        return True

print(isValid('()'))

# Another way to code this
def isValid1(s):
    myMap = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for c in s:
        if c in myMap:
            stack.append(c)
        else:
            if not stack or c != myMap[stack[-1]]:
                return False
            else:
                stack.pop()
    return not stack
print(isValid1('()'))
