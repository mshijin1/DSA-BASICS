# class Solution1:
#     def __init__(self):
#         self.sum=0
        
#     def sum_of_n(self,n):
#         if n==0:
#             return 0
#         return (n*(n+1)) // 2
        
# result=Solution1().sum_of_n(5)
# # Using formulae
# print(" Using formulae", result)


class Solution2:
    def sum_of_n(self,n):
        if n==0:
            return 0
        print(n)
        return n + self.sum_of_n(n-1)
        
result=Solution2().sum_of_n(int(input("Enter a number:...")))
# using recurssion
print(" Using recurrsion", result)