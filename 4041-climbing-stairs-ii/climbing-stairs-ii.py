class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + costs[j - 1] + 1
            if j >= 2:
                dp[j] = min(dp[j], dp[j - 2] + costs[j - 1] + 4)
            if j >= 3:
                dp[j] = min(dp[j], dp[j - 3] + costs[j - 1] + 9)
                
        return dp[n]