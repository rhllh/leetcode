"""
You are given a string s and an integer k. You can choose any character of the string and change it 
to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
def charReplace(s, k):
    # substring, sliding window
    # set L and R to 0, keep expanding and check if windowLen - freq(mostFreqChar) <= k
    # update R and update freq map
    # replace chars of lower freq to the char with largest freq as we want to minimise
    # no of replacements since we have a limit of k
    # if hit k, need to shrink window using L and update freqs
    
    res = 0
    l = 0
    freq = {}
    
    for r in range(len(s)):
        freq[s[r]] = 1 + freq.get(s[r],0)
        
        while (r-l+1) - max(freq.values()) > k:     # check windowLen - freq(mostFreqChar) exceeded k
            freq[s[l]] -= 1                  # remove letter at l
            l += 1                           # update l pointer to shrink window
            
        res = max(res, r-l+1)
        
    return res

print(charReplace(s = "AABABBA", k = 1))