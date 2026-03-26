# class Solution:
#     def factorial(self, num):
#         if num==0:
#             return 0
#         result=1
#         for i in range(num):
#             result=result*num
#             num=num-1
#         return result
# obj=Solution()
# result=obj.factorial(int(input("Enter a number: ")))
# print("Factorial of a number is: ", result)


class Solution:
    def factorial(self, num):
        if num==0:
            return 0
        result=1
        for i in range(1, num+1):
            result=result*i
        return result
obj=Solution()
result=obj.factorial(int(input("Enter a number: ")))
print("Factorial of a number is: ", result)