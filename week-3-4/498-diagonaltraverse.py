"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""
def diagonal(mat):
    # sum of indices of a diagonal is a constant
    # odd diagonals go from L-> R
    # even go R->L
    d = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # map locations to sum of indices in map
            if i+j not in d:
                d[i+j] = [mat[i][j]]
            else:
                d[i+j].append(mat[i][j])
    
    res = []
    for entry in d.items():     # i+j : mat[i][j]
        if entry[0] % 2 == 0:
            # even diagonals (reverse)
            [res.append(x) for x in entry[1][::-1]]
        else:
            [res.append(x) for x in entry[1]]
            
    return res

print(diagonal([[1,2,3],[4,5,6],[7,8,9]]))