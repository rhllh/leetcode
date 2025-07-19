"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, 
either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color
if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
"""

def floodFill(image, sr, sc, color):
    startColor = image[sr][sc]
    m, n = len(image), len(image[0])
    if startColor == color:
        return image
    
    def fill(image, r, c, color):
        if (r < 0 or r >= m or c < 0 or c >= n or image[r][c] != startColor):
            return
        
        image[r][c] = color
        
        fill(image, r-1, c, color)
        fill(image, r+1, c, color)
        fill(image, r, c-1, color)
        fill(image, r, c+1, color)
        
    fill(image, sr, sc, color)
    
    return image
    
print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))   # [[2,2,2],[2,2,0],[2,0,1]]
print(floodFill([[0,0,0],[0,0,0]], 0, 0, 0))    # [[0,0,0],[0,0,0]]