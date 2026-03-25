import math
class Solution:
    def isArmstrong(self, n:int) -> bool:
        digits = int(math.log10(n)+1)
        return sum(int(i)**digits for i in str(n)) ==n
    
obj=Solution()
result=obj.isArmstrong(153)
print(result)