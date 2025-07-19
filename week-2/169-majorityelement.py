"""
Given an array nums of size n, 
return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. <--- VERY IMPORTANT!!
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
def majorityElement(nums):
    ans, count = 0, 0
    
    # O(n) time and space
    # freq = {}
    
    # for n in nums:
    #     freq[n] = 1 + freq.get(n,0)
    #     if freq[n] > count:
    #         ans = n
    #         count = freq[n]
    
    # O(n) time O(1) space
    for n in nums:
        if count == 0:
            ans = n
        count += (1 if n == ans else -1)
                
    return ans

print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([2,2,1,1,1,2,3])) # invalid because two majority elements
print(majorityElement([2,2,1,1,1,2,2,3]))
print(majorityElement([3,2,3,2,4,3])) # these two are invalid because count of 3 is not > 6/2 
print(majorityElement([3,3,3,4,2,2])) #