class Solution:
    def findGCD(self, num1: str, num2: int) -> int:
        gcd:int=1
        for i in range(1, min(num1, num2)+1):
            if num1%i==0 and num2%i==0:
                gcd=i
                print(gcd)
        return gcd
obj=Solution()
result=obj.findGCD(20,15)
print(result)
        