def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    fact=3
    while fact*fact<=n:
        if n%fact==0:
            return False
        fact+=2
    return True
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        ans=0
        for i in range(len(nums)):
            a=nums[i][i]
            b=nums[i][n-i-1]
            if is_prime(a):
                ans=max(ans,a)
            if is_prime(b):
                ans=max(ans,b)
        return ans

        


        