class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product 

        prefix = [1] * len(nums)

        # From left to right, we need to multiple the previous index by the previous left side prefix
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # From right to left, multiply the prefix by the suffix before, then update suffix with new num
        suffix = 1
        for j in range(len(nums) - 1, -1 , -1):
            prefix[j] *= suffix
            suffix *= nums[j]
        
        return prefix