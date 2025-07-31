"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
def combiSum(candidates, target):
    # backtracking question (DFS)
    # base case: sum = target, i >= len(candidates) or sum > target
    # decisions to make:
    #   include candidates[i] in current "path"
    #   cannot include, so remove it from "path"
    
    res = []
    
    def dfs(i, curr, total):
        if total == target:         # found solution, append combination to res
            res.append(curr.copy())
            return
        if i >= len(candidates) or total > target:      # out of bounds
            return
        
        # make choice
        curr.append(candidates[i])
        dfs(i, curr, total+candidates[i])       # if use i, can keep using it until it hits base case
        
        # undo choice
        curr.pop()                          # go to next candidate after have traversed all paths of i
        dfs(i+1, curr, total)               # so we don't ever use i in i+1's paths
        
    dfs(0,[],0)
    return res

print(combiSum([2,3,5],8))