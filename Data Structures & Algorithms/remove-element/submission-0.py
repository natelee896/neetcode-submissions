class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pointer = 0

        for i, num in enumerate(nums):
            if num != val:
                nums[pointer] = num
                pointer += 1
        
        return pointer