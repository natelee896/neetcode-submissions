class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums) 
        result = 0

        # Go through each unique, and try to get the start of the sequence
        for num in uniques:
            if num - 1 not in uniques:
                curr = num
                length = 1
                while curr + 1 in uniques:
                    curr += 1
                    length += 1
                result = max(length, result)
    
        return result
            


