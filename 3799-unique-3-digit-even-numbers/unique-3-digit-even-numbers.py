import itertools
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=set()
        for i in itertools.permutations(digits,3):
            if i[0]==0:
                continue
            d=i[0]*100+i[1]*10+i[2]*1
            if d%2==0:
                res.add(d)
        return len(res)
        

        