class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            h = min(heights[left], heights[right])

            max_water = max(max_water, length * h)

            if h == heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_water