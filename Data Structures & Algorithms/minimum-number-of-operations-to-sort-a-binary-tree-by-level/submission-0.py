# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)

        result = 0

        while q:
            length = len(q)
            level = []

            for i in range(length):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result += self.cycleSortSwaps(level)
        
        return result

    def cycleSortSwaps(self, arr):
        target = {v: i for i, v in enumerate(sorted(arr))}
        swaps = 0
        for i in range(len(arr)):
            while target[arr[i]] != i:          # keep going until the right value lands here
                j = target[arr[i]]
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        return swaps