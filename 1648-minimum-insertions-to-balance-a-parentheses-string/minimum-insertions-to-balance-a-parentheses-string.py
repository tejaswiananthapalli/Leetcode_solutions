class Solution:
    def minInsertions(self, s: str) -> int:
        ans=0
        open_need=0
        i=0
        n=len(s)
        while i<n:
            if s[i]=='(':
                open_need+=1
                i+=1
            else:
                if (i+1)<n and s[i+1]==')':
                    i+=2
                else:
                    ans+=1
                    i+=1
                if open_need>0:
                    open_need-=1
                else:
                    ans+=1
        ans+=open_need*2
        return ans
        