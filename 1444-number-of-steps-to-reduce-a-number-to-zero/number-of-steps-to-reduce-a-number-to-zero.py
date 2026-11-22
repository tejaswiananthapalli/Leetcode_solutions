import math
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step=0
        while(num>0):
            if (num%2==0):
                step+=1
                num/=2
            else:
                num=num-1
                step+=1
                
        return step

        
      
        
        