class Solution:
    def isPrime(sef, n:int)-> bool:
        
        if n<=0:
            return False
        cnt=0
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                cnt +=1
                
                if n // i !=i:
                    cnt +=1
        if cnt==2:
            return True
        else:
            return False
    
obj=Solution()
result=obj.isPrime(12)
print(result)