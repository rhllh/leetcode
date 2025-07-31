"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
def longestConsecSeq(nums):
    # consec sequence: seq of elem where each elem is exactly one greater than previous
    # elements in answer may not be consecutive in the original array
    # identify start of sequence by checking in num-1 exists in the array => hashset
    
    seen = set(nums)
    longest = 0
    
    for n in seen:      # fix at one element
        if (n-1) not in seen:
            # it is the start of sequence
            length = 1
            
            while (n + length) in seen:     # increment element and check if it is in seen
                length += 1                 # sequence size increases
                
            longest = max(longest, length)
            
    return longest

print(longestConsecSeq([0,3,7,2,5,8,4,6,0,1]))