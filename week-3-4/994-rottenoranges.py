"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
def rottingOranges(grid):
    # BFS
    EMPTY, FRESH, ROTTEN = 0, 1, 2
    m, n = len(grid), len(grid[0])
    q = deque()
    freshCnt = 0
    
    # get freshCnt or add rotten to queue
    for i in range(m):
        for j in range(n):
            if grid[i][j] == FRESH:
                freshCnt += 1
            elif grid[i][j] == ROTTEN:
                q.append((i,j))
                
    # all fresh already
    if freshCnt == 0:
        return 0
    
    minutes = -1
    while q:
        q_size = len(q)                 # may change with every iteration
        minutes += 1
        for _ in range(q_size):
            i, j = q.popleft()          # check at this rotten location and remove to not double count
            for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:       # all its adjacent cells
                if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:   # if any are fresh, make them rotten
                    grid[r][c] = ROTTEN
                    freshCnt -= 1                   # decrement number of fresh oranges
                    q.append((r,c))                 # we added a new rotten orange, so add it to queue to check for adjacent cells
                    
    if freshCnt == 0:
        return minutes
    else:
        return -1
    
print(rottingOranges([[2,1,1],[1,1,0],[0,1,1]]))