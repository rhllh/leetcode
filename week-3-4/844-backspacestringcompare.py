"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 
Follow up: Can you solve it in O(n) time and O(1) space?
"""
# using stack O(n) space, O(n) time
def compareStack(s, t):
    def backspace(s):
        stack = []
        for c in s:
            if c == "#" and stack:
                # stack not empty so can backspace
                stack.pop()
            elif c != "#":
                stack.append(c)
                
        return stack
    
    return backspace(s) == backspace(t)


# using 2 pointers O(1) space, O(n) time
def comparePointer(s, t):
    # helper function
    def getNextValidChar(s, end):
        backspaceCnt = 0
        
        while end >= 0:
            if s[end] == "#":           # if meet #, "remove" or skip to next character
                backspaceCnt += 1
            elif backspaceCnt > 0:      # if not # but has backspace, decrement the count
                backspaceCnt -= 1
            else:                       # return the index when not # and no more to backspace
                break
            
            end -= 1
            
        return end
    
    # iterate strings from the end
    ps = len(s)-1
    pt = len(t)-1
    
    # continue until both pointers are at the beginning
    while ps >= 0 or pt >= 0:
        ps = getNextValidChar(s, ps)
        pt = getNextValidChar(t, pt)
        
        # base cases
        if ps < 0 and pt < 0:   # both strings empty
            return True
        
        if ps < 0 or pt < 0:    # one string empty
            return False
        elif s[ps] != t[pt]:    # if valid character, should be the same
            return False
        
        # traverse backwards
        ps -= 1
        pt -= 1
        
    return True

print(compareStack(s = "a#c", t = "b"))
print(comparePointer(s = "a#c", t = "b"))