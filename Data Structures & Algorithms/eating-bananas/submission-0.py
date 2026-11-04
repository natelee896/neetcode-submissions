class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.eatingPiles(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def eatingPiles(self, piles, mid):
        result = 0
        for pile in piles:
            result += math.ceil(pile / mid)
        
        return result