# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS, just needs to compare to the max thus far in the path
        self.count = 0

        def dfs(node, currMax):
            if not node:
                return 
            if node.val >= currMax:
                self.count += 1
            currMax = max(currMax, node.val)
            dfs(node.left, currMax)
            dfs(node.right, currMax)

        dfs(root, float('-inf')) 
        return self.count          
