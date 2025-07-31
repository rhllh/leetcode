"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
def permInString(s1, s2):
    # substring, sliding window
    # slide window on B using fixed length of string A
    # length A must be < B
    # track char freqs of A and B
    # for a substring in B, freq of chars will match the freq of chars in A = 26 (every char match)
    if len(s1) > len(s2):
        return False

    s1c, s2c = [0] * 26, [0] * 26
    # populate first len(s1) characters
    for i in range(len(s1)):
        s1c[ord(s1[i])-ord('a')] += 1
        s2c[ord(s2[i])-ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1c[i] == s2c[i]:
            matches += 1

    l = 0
    # sliding window after first len(s1) chars
    for r in range(len(s1),len(s2)):
        if matches == 26:
            return True

        # add chars by moving R
        idx = ord(s2[r])-ord('a')       # index in s2 since we are traversing s2
        s2c[idx] += 1               # add
        if s1c[idx] == s2c[idx]:
            matches += 1
        elif s1c[idx] + 1 == s2c[idx]:
            matches -= 1

        # remove chars by moving L
        idx = ord(s2[l])-ord('a')
        s2c[idx] -= 1               # remove
        if s1c[idx] == s2c[idx]:
            matches += 1
        elif s1c[idx] - 1 == s2c[idx]:
            matches -= 1
        
        l += 1

    return matches == 26

print(permInString(s1 = "ab", s2 = "eidbaooo"))
print(permInString(s1 = "ab", s2 = "eidboaoo"))