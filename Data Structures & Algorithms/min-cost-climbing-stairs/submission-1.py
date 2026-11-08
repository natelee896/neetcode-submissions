class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (len(cost) + 1)
        # DP: dp[i] means how could I have gotten here
        # DP: cheapest way to reach floor i from either one step back or two

        for i in range(2, len(cost) + 1):
            # Subproblem: min between stepping from the last step or the 2 steps before
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]