class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if candidate is None:
                candidate = num
                count = 1
            elif candidate != num:
                count -= 1
            elif candidate == num:
                count += 1
            
            if count < 0:
                candidate = num
                count = 0
        
        return candidate
