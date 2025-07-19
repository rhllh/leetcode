"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""
def climbStairs(n):
    # DP (memoization)
    if n <= 1:
        return 1
    
    memo = [0] * (n)
    memo[0] = 1
    memo[1] = 2
    
    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[-1]

def climbStairs2(n):
    # DP (constant space)
    first, second = 1, 1
    
    for i in range(n-1):
        temp = first
        first = first+second
        second = temp
        
    return first
    
print(climbStairs(5))
print(climbStairs(4))
print(climbStairs(3))
print(climbStairs(2))
print(climbStairs(1))
print()
print(climbStairs2(5))
print(climbStairs2(4))
print(climbStairs2(3))
print(climbStairs2(2))
print(climbStairs2(1))