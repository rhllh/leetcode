"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k

Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 
Constraints:
1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
"""
def findPairsSort(nums, k):
    # sort -> O(nlogn) time
    # 2 pointer -> O(1) space
    
    nums.sort()
    i, j = 0, 1
    count = 0
    
    while j < len(nums):
        diff = abs(nums[i]-nums[j])
        
        if diff == k:
            count += 1      # found a pair
            i += 1      # go to next pair of indices
            j += 1
            while j < len(nums) and nums[i] == nums[i-1] and nums[j] == nums[j-1]:      # check for uniqueness and within boundaries
                i += 1
                j += 1
        elif diff > k:      # diff is too large, make numbers closer to each other by increasing i
            i += 1
        else:           # make numbers further from each other by increasing j
            j += 1
            
        if i == j:      # make numbers further from each other by increasing j
            j += 1
            
    return count

from collections import Counter
def findPairsMap(nums, k):
    hm = Counter(nums)      # track frequency of elements in nums

    count = 0
    for n in hm:            # for each element
        if k == 0:          # if no difference, then any two indexes with the same element can get diff 0
            if hm[n] >= 2:
                count += 1      # add one pair
        else:               # if there is difference,
            if n + k in hm:         # find complement in hashmap
                count += 1          # add a pair if exists, will not add the same pair twice

    return count

print(findPairsSort(nums = [3,1,4,1,5], k = 2))
print(findPairsMap(nums = [3,1,4,1,5], k = 2))