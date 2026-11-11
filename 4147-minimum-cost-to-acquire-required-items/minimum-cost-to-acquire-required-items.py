class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        ans = common * min(costBoth, cost1 + cost2)
        
        rem1 = need1 - common
        rem2 = need2 - common
        
        if rem1 > 0:
            ans += rem1 * min(costBoth, cost1)
        if rem2 > 0:
            ans += rem2 * min(costBoth, cost2)
            
        return ans