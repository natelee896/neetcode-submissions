class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        # bitwise op

        result = 0

        for num in nums:
            result ^= num
        
        return result
