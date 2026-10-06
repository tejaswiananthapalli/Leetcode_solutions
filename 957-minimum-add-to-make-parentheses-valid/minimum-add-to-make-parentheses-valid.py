class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_par=0
        close_par=0
        for ch in s:
            if ch=='(':
                open_par+=1
            else:
                if open_par>0:
                    open_par-=1
                else:
                    close_par+=1
        return open_par+close_par
        