class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            first = nums[i]

            if first > 0:
                break
            
            if i > 0 and first == nums[i - 1]: # no dupes
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                combined = first + nums[left] + nums[right]

                if combined == 0:
                    result.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif combined > 0:
                    right -= 1
                else:
                    left += 1
            
        return result
