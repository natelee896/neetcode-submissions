class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = defaultdict(int)

        for i, num in enumerate(nums):
            comp = target - num
            if comp in complements:
                return [complements[comp], i]
            complements[num] = i
        
        return [-1, -1]