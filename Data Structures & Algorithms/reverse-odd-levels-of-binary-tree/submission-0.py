# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque()
        q.append(root)
        curr_level = 0

        while q:
            length = len(q)
            level = []

            for i in range(length):
                node = q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr_level % 2 == 1:
                left = 0
                right = len(level) - 1

                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
            curr_level += 1

        return root