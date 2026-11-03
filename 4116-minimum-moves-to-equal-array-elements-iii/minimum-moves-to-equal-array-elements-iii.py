class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        sums=0
        for i in range(len(nums)):
            sums+=m-nums[i]
        return sums
        