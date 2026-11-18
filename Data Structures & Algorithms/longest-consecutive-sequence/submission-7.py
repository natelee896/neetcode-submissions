class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        result = 0

        for num in uniques:
            if num - 1 not in uniques: # found the starting position
                curr = num
                length = 1
                
                while curr + 1 in uniques:
                    length += 1
                    curr += 1

                result = max(length, result)
        
        return result