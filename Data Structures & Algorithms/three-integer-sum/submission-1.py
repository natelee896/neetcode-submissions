class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        nums.sort()

        for i in range(len(nums)):
            first = nums[i]
            if first > 0:
                break
            
            if i > 0 and first == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = first + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result