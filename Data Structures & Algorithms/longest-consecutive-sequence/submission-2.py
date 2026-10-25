class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0

        for num in uniques:
            # if its the possible start of a sequence
            if num - 1 not in uniques:
                curr = num
                length = 1
            
                while curr + 1 in uniques:
                    curr += 1
                    length += 1

                longest = max(length, longest)
        
        return longest