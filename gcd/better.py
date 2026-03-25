class Solution:
    def findGCD(self, num1, num2):
        gcd:int=1
        for i in range (max(num1, num2), 0 , -1):
            if num1%i==0 and num2%i==0:
                return i
        return 1
    
obj=Solution()
result=obj.findGCD(20, 15)
print(result)