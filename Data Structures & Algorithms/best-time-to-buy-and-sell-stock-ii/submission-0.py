class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = float('inf')
        profit = 0

        for price in prices:
            bestBuy = min(price, bestBuy)
            if price > bestBuy:
                profit += price - bestBuy
                bestBuy = price
        
        return profit