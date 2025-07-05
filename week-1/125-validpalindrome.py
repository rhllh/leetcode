"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
# solution 1

"""
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())        # uses built-in function
    l, r = 0, len(s)-1                  # two pointer so we work on same string
    
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1

    return True
"""

# solution 2
# extra memory for additional string

"""
def isPalindrome(s):
    return s == s[::-1]
"""
    
# solution 3
# less memory but longer run time

def isPalindrome(s):
    l, r = 0, len(s)-1
    
    while l < r:
        while l < r and not isAlnum(s[l]):
            l = l + 1
        while r > l and not isAlnum(s[r]):
            r = r - 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l+1, r-1
        
    return True

def isAlnum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

print(isPalindrome("A man, a plan, a canal: Panama"))   # true
print(isPalindrome(" "))        # true