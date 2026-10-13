class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        bit_counts = [0] * 31
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        max_nums = [0] * k
        for i in range(k):
            current_num = 0
            for bit in range(31):
                if bit_counts[bit] > 0:
                    current_num |= (1 << bit)
                    bit_counts[bit] -= 1
            max_nums[i] = current_num
            
        total_sum = 0
        for num in max_nums:
            total_sum = (total_sum + num * num) % MOD
            
        return total_sum
        