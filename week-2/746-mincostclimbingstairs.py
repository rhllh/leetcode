"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
# memoization
def minCost(cost):
    memo = [-1] * len(cost)
    
    def dfs(i):
        if i >= len(cost):      # past bounds of array, cost = 0
            return 0
        if memo[i] != -1:       # return cached value
            return memo[i]
        memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))     # include cost at ith step + min cost between taking 1 or 2 steps
        
        return memo[i]
        
    return min(dfs(0), dfs(1))      # start at index 0 or 1

# bottom-up
def minCost2(cost):
    n = len(cost)
    dp = [0] * (n+1)
    
    for i in range(2, n+1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
    return dp[n]

# space optimised - modify array in place
def minCost3(cost):
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i], cost[i-1])  # iteratively add costs at every index, cost to add is the min of itself and costs before it
        
    return min(cost[n-1], cost[n-2])        # get min of taking 1 or 2 steps to n

print(minCost([10,15,20]))
print(minCost2([10,15,20]))
print(minCost3([10,15,20]))