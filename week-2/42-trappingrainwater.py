"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
# O(n) time, O(n) space
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    maxL = [0] * n      # O(n) array
    maxR = [0] * n
    
    maxL[0] = height[0]     # set left boundary
    for i in range(1,n):
        maxL[i] = max(maxL[i-1], height[i])
        
    maxR[n-1] = height[n-1]     # set right boundary
    for i in range(n-2, -1, -1):
        maxR[i] = max(maxR[i+1], height[i])
        
    res = 0
    for i in range(n):
        res += min(maxL[i], maxR[i]) - height[i]
        
    return res

# O(n) time, O(1) space
def trap2(height):
    if not height:
        return 0
    
    # initialise left and right boundary
    l, r = 0, len(height)-1
    maxL, maxR = height[l], height[r]
    res = 0
    
    while l < r:
        # shift the pointer at the smaller max value
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])     # update maxL
            res += maxL - height[l]         # similar to min(maxL, maxR) - height
        else:
            r -= 1
            maxR = max(maxR, height[r])
            res += maxR - height[r]
            
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))