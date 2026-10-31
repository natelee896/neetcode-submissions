class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos_nums = set()
        
        for num in nums:
            if num > 0:
                pos_nums.add(num)
        
        min_pos = 1
        if len(pos_nums) == 0:
            return min_pos
        
        while min_pos in pos_nums:
            min_pos += 1
        
        return min_pos
        
