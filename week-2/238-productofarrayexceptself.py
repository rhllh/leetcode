"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
"""

def prod(arr):
    # using division
    prd = 1
    for i in arr:
        prd *= i
        
    output = [1] * (len(arr))
    for i in range(len(output)):
        output[i] = prd // arr[i]
        
    return output

def prod2(arr):
    # using prefix and postfix
    output = [1] * len(arr)
    
    pre = 1
    for i in range(len(arr)):
        output[i] = output[i] * pre
        pre = pre * arr[i]
        
    post = 1
    for i in range(len(arr)-1,-1,-1):
        output[i] = output[i] * post
        post = post * arr[i]
        
    return output
    

print(prod([1,2,4,6]))
print(prod2([1,2,4,6]))