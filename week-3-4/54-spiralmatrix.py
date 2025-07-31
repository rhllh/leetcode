"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
def spiralMatrix(grid):
    # 4 pointers for left, right, top, bottom boundaries
    res = []
    left, right = 0, len(grid[0])   # right and bottom are out of bounds initially
    top, bottom = 0, len(grid)
    
    while left < right and top < bottom:
        for i in range(left, right):        # add top row
            res.append(grid[top][i])
        top += 1                            # move top pointer down
        
        for i in range(top, bottom):        # right col will not overlap with top row (rightmost elem) as top pointer was updated
            res.append(grid[i][right-1])    # add right col
        right -= 1                          # move right pointer left
            
        if not (top < bottom and left < right):
            break
        
        for i in range(right-1, left-1, -1):    # bottom row (backwards)
            res.append(grid[bottom-1][i])
        bottom -= 1                             # move bottom pointer up
        
        for i in range(bottom-1, top-1, -1):    # left col
            res.append(grid[i][left])
        left += 1                               # move left pointer right
        
    return res
        
print(spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))