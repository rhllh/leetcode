"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()[]{}"
Output: true

Example 2:

Input: s = "(]"
Output: false

Example 3:

Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
    pair = {')': '(', ']': '[', '}': '{'}
    stack = []
    for b in s:
        if b in pair:
            # b is a closing bracket
            if stack and stack[-1] == pair[b]:
                # check latest bracket in stack which means it cannot be empty
                # check that it is the corresponding open bracket to b
                stack.pop()
            else:
                # we cannot start a stack with a closing bracket
                return False
        else:
            # it is an open bracket so add it to the stack
            stack.append(b)

    return len(stack) == 0

print(isValid("()[]{}"))    # true
print(isValid("((()"))      # false
print(isValid("[)"))        # false
print(isValid("{[()]}"))    # true