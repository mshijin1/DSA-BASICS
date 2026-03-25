import math
def count_digits(n):
    # sum=0
    
    # while n>0:
    #     m=n%10
    #     sum+=m
    #     n=n//10
    # return sum
    
   cnt = int(math.log10(n)+1)
   return cnt

result=count_digits(12345)

print(result)