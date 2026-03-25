class Solution:
    def print_all_divisors(self, n):
        list=[]
        for i in range(1, n+1):
            if n%i==0:
                list.append(i)
        return list
obj=Solution()
list=obj.print_all_divisors(22)
print(list)