"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from collections import deque
def updateMatrix(mat):
    # BFS
    # change non-zero cells to infinity and enqueue the zero cells
    # only update the non-zero cells
    
    rows, cols = len(mat), len(mat[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque()
    
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                q.append((i,j))
            else:
                mat[i][j] = float('inf')
                
    while q:
        r, c = q.popleft()      # go to non-zero location
        
        for dr, dc in dirs:     # go to adjacent cells
            new_r, new_c = r+dr, c+dc
            
            if 0 <= new_r < rows and 0 <= new_c < cols and \
                mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1           # current cell add distance from prev cell
                    q.append((new_r,new_c))
                    
    return mat
    
    
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))