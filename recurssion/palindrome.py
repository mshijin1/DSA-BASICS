# Using iterative approch
# class Solution:
#     def palindrome_iteration(self, s):
#         if len(s) <= 1:
#             return "please enter a string whoose length is greater than 1"
#         for i in range(len(s) // 2):
#             if s[i] != s[len(s) - 1 - i]:
#                 return f"The string '{s}' is not a palindrome"
#         return f"'{s}' is a palindrome"

# obj=Solution()
# result=obj.palindrome_iteration(input("Enter your String: "))
# print(result)

# using recurssinve approach

class Solution:
    def palindrome_recurssion(self, i, s):
        if i >= len(s) // 2:
            return True
        if s[i] !=s[len(s)-i-1]:
            return False
        
        return self.palindrome_recurssion(i+1, s)
    
result=Solution().palindrome_recurssion(0, input("Enter your String: "))
if result:
    print("The string is a palindrome")
else:   
    print("The string is not a palindrome")