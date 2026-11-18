class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, path, total):
            if total == target:
                result.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()
            return
        
        backtrack(0, [], 0)
        return result