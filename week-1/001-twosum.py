"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. Only one valid answer exists.

Example 1:

Input: nums = [2,7,11,15], target = 9
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

def twoSum(nums, target):
    d = dict()
    for i in range(len(nums)):
        if (target-nums[i]) in d:
            # there is only one solution, so we can return immediately
            return [d[target-nums[i]], i]
        else:
            # store the index of the current number
            # if we find the complement later, we can return it
            d[nums[i]] = i

    return -1

print(twoSum([2,7,11,15], 9))   # [0,1]
print(twoSum([3,2,4], 6))       # [1,2]
print(twoSum([3,3], 6))         # [0,1]