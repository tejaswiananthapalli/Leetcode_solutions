class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        freq={}
        ans=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for i in freq:
            if freq[i]==1:
                res.append(i)
        return res
        