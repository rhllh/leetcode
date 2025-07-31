"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Exmaple 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
def searchMatrix(matrix, target):
    # each row sorted in non-descending order -> apply BS
    # 1st integer of each row is larger than last integer of previous row
    # must be O(log(m*n)) time => traverse matrix once + log implies BS
    # eliminate rows, then each row is an array (1d) for normal BS
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS-1
    
    # find the row index that target is in
    while top <= bot:
        midr = top + (bot-top)//2
        if target < matrix[midr][0]:        # check 1st integer to eliminate all rows below
            bot = midr-1
        elif target > matrix[midr][COLS-1]:     # check last integer to eliminate all rows above
            top = midr+1
        else:
            break               # found the row it is in
        
    if not (top <= bot):        # check boundaries of top and bottom pointer
        return False
    
    # regular BS within the row
    left, right = 0, COLS-1
    while left <= right:
        midc = left + (right-left)//2
        if target > matrix[midr][midc]:
            right = midc-1
        elif target < matrix[midr][midc]:
            left = midc+1
        else:
            return True
        
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))