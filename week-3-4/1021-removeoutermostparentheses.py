"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, 
and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it 
into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, 
where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"

Constraints:
1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
"""
def removeOuterParentheses(s):
    res = []
    start, balance = 0, 0
    
    # track the valid parentheses group
    for i, ch in enumerate(s):
        if ch == "(":
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            # add innermost bracket so exclude first and last parentheses
            res.append(s[start + 1:i])
            # update start pointer
            start = i + 1
            
    return ''.join(res)

print(removeOuterParentheses("(()())(())(()(()))"))