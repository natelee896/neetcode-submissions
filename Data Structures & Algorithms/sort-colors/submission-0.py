class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low, medium, high = 0, 0, len(nums) - 1

        while medium <= high:
            if nums[medium] == 0:
                nums[medium], nums[low] = nums[low], nums[medium]
                medium += 1
                low += 1
            elif nums[medium] == 1:
                medium += 1
            else:
                nums[medium], nums[high] = nums[high], nums[medium]
                high -= 1
            
        return 

            