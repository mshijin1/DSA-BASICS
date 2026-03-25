class Solution:
    def findGCD(self, num1, num2):
        while num1>0 and num2>0:
            if num1>num2:
                num1=num1%num2
            else:
                num2=num2%num1
                
        if num1==0:
            return num2
        else:
            return num1

obj=Solution()
result=obj.findGCD(20, 15)
print(result)