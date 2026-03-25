class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            return str(x)==str(x)[::-1]
        
obj=Solution()
result=obj.isPalindrome(12211)
print(result)