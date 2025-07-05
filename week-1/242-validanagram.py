"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def isAnagram(s, t):
    # solution 1
    """
    # built-in function
    return sorted(s) == sorted(t)
    """
    
    # solution 2
    """
    # extra memory, time O(s+t)
    # good for unicode characters
    if (len(s) != len(t)):
        return False
    
    s_dict, t_dict = dict(), dict()

    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    for j in t:
        if j in t_dict:
            t_dict[j] += 1
        else:
            t_dict[j] = 1

    return s_dict == t_dict
    """

    # solution 3
    # constant memory, time O(s+t)
    # good for unicode characters
    if (len(s) != len(t)):
        return False
    
    counter = {}
    
    for i in s:
        counter[i] = counter.get(i, 0) + 1
        
    for j in t:
        if j not in counter or counter[j] == 0:
            return False
        else:
            counter[j] = counter[j] - 1
            
    return True
    
    # solution 4
    """
    # ascii values
    # constant memory, time O(s+t)
    # alphabet only
    if (len(s) != len(t)):
        return False
    
    arr = [0] * 26
    
    for char in s:
        arr[ord(char) - ord('a')] += 1
        
    for char in t:
        if arr[ord(char) - ord('a')] == 0:
            return False
        arr[ord(char) - ord('a')] -= 1 
        
    return True
    """

print(isAnagram("anagram","nagaram"))   # true