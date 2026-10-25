class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = float('inf')
        profit = float('-inf')

        for price in prices:
            bestBuy = min(bestBuy, price)
            profit = max(profit, price - bestBuy)
        
        return profit