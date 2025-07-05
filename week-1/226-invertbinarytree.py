"""
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth-first search
        if not root:            # return to previous node if current is null
            return

        # swap children
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)      # continue down left tree
        self.invertTree(root.right)     # continue down right tree if unexplored

        return root