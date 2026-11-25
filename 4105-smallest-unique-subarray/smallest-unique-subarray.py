from typing import List
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761
        
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        
        for i in range(n):
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2
            h1[i + 1] = (h1[i] * BASE1 + nums[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + nums[i]) % MOD2
            
        def has_unique(length: int) -> bool:
            counts = Counter()
            b1 = p1[length]
            b2 = p2[length]
            for i in range(n - length + 1):
                val1 = (h1[i + length] - h1[i] * b1) % MOD1
                val2 = (h2[i + length] - h2[i] * b2) % MOD2
                counts[(val1, val2)] += 1
            return 1 in counts.values()

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans