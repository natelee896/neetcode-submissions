class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = float('inf')
        bestProfit = float('-inf')

        for price in prices:
            bestBuy = min(price, bestBuy)
            bestProfit = max(bestProfit, price - bestBuy)

        return bestProfit