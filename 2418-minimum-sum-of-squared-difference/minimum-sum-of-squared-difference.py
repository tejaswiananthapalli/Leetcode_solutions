class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        abs_diff = [0] * n 
        for i in range(n) :
            abs_diff[i] = abs(nums1[i] - nums2[i])
        k_total = k1 + k2
        if k_total >= sum(abs_diff):
            return 0
        max_diff_val = 0
        for diff in abs_diff :
            max_diff_val = max(max_diff_val,diff)
        counts = [0] * (max_diff_val + 1)
        for diff in abs_diff :
            counts[diff] += 1
        for i in range(max_diff_val,0,-1):
            if k_total == 0 :
                break
            if counts[i] > 0 :
                if k_total >= counts[i]:
                    k_total -= counts[i]
                    counts[i-1] += counts[i]
                    counts[i] = 0
                else :
                    counts[i-1] += k_total
                    counts[i] -= k_total
                    k_total = 0
                    break
        min_sum_sq_diff = 0
        for i in range(max_diff_val + 1):
            min_sum_sq_diff += i * i * counts[i]
        return min_sum_sq_diff
        
        