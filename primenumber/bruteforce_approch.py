class Solution:
    def isPrime(sef, n:int)-> bool:
        cnt=0
        for i in range(1, n+1):
            if n%i==0:
                cnt=cnt+1
        if cnt==2:
            return True
        else:
            return False
    
obj=Solution()
result=obj.isPrime(2)
print(result)