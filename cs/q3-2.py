"""
Given two strings, merge them with the following merge function: instead of comparing the characters in the usual 
lexicographical order, compare them based on how many times they occur in their respective strings. 
Fewer occurrences mean the character is considered smaller; in case of equality, compare them lexicographically; 
in case of equality, take the character from the first string.
"""
from collections import defaultdict
def mergeByCount(s, t):
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)
    
    for c in s:
        s_dict[c.lower()] += 1
        
    for c in t:
        t_dict[c.lower()] += 1
        
    i, j = 0, 0
    ans = ""
    while i < len(s) and j < len(t):
        if s_dict[s[i].lower()] < t_dict[t[j].lower()]:
            ans += s[i]
            i += 1
        elif s_dict[s[i].lower()] > t_dict[t[j].lower()]:
            ans += t[j]
            j += 1
        else:
            if s[i] < t[j]:
                ans += s[i]
                i += 1
            elif s[i] > t[j]:
                ans += t[j]
                j += 1
            else:
                ans += s[i]
                i += 1
            
    if i < len(s):
        ans += s[i:]
    if j < len(t):
        ans += t[j:]
        
    return ans

    
    
print(mergeByCount("Sundays","Movies"))
print(mergeByCount("Suunday","Movvies"))