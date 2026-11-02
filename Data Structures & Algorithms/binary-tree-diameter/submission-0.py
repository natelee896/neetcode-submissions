# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        self.best = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            self.best = max(self.best, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.best
        
