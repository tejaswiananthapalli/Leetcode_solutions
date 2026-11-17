class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
                    
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                for d in divisors[length]:
                    changes = 0
                    for rem in range(d):
                        left = i + rem
                        right = j - (d - 1 - rem)
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
                
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                for m in range(2 * (j - 1), i - 1):
                    if dp[m][j - 1] + cost[m][i - 1] < dp[i][j]:
                        dp[i][j] = dp[m][j - 1] + cost[m][i - 1]
                        
        return dp[n][k]