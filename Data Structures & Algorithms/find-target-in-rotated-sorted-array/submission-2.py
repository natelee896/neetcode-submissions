class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        
        pivot = left

        def binarySearch(left, right):
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        result = binarySearch(0, pivot - 1)
        if result != -1:
            return result
        return binarySearch(pivot, len(nums) - 1)