class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        n=min(nums)
        a=[]
        for i in range(len(nums)):
            a.append(m-nums[i])
        return sum(a)
        