"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1
"""
# move = walk from one land cell to adjacent land cell OR to boundary of grid

def numEnclavesDFS(grid):
    # DFS like no of islands question
    # assume can modify in place
    m, n = len(grid), len(grid[0])
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
    
        grid[i][j] = 0
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        
    res = 0
    for i in range(m):
        for j in range(n):
            # check grid on its boundary. if 1, set to 0
            if (i == 0 or j == 0 or i == m-1 or j == n-1) \
                and grid[i][j] == 1:
                    dfs(i,j)
                    
    for i in range(m):
        for j in range(n):
            res += grid[i][j]
            
    return res


def numEnclavesNoInPlace(grid):
    # assume no modify in place
    m, n = len(grid), len(grid[0])
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 \
            or (i,j) in visit:      # check if out of bounds or is not land or is visited cell
            return 0                # no need to add this cell

        visit.add((i,j))            # visited add to set
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        res = 1         # current cell
        for dr, dc in dirs:         # check and add any adjacent land cells
            res += dfs(i+dr,j+dc)

        return res
    
    visit = set()
    land, borderland = 0, 0
    for i in range(m):
        for j in range(n):
            land += grid[i][j]          # will add all the lands since land = 1 and sea = 0
            if (grid[i][j] and (i,j) not in visit) and \
                (j in [0,n-1] or i in [0,m-1]):         # not visited cell and is on the boundary
                    borderland += dfs(i,j)
                    
    return land-borderland

print(numEnclavesDFS([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(numEnclavesNoInPlace([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))