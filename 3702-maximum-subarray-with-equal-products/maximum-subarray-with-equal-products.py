import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        
        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                elif prod > l * g * 2520:
                    break
                    
        return ans