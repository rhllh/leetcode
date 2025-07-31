"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""
def toeplitz(grid):
    # check each elem == top left neighbour
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i-1 < 0 or j-1 < 0:
                continue
            
            if grid[i][j] != grid[i-1][j-1]:
                return False
            
    return True

print(toeplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))