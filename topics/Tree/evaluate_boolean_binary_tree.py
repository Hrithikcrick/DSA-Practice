from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root.left is None and root.right is None:
            if root.val == 1:
                return True
            else:
                return False

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val == 2:
            return left or right
        else:
            return left and right

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
