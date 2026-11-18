class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left 
            h = min(heights[right], heights[left])
            max_water = max(max_water, width * h)

            if h == heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_water