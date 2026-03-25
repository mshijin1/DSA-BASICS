class Solution:
    def print_all_divisors(self, n):
        list=[]
        for i in range(1, int(n**0.5) +1):
            if n%i==0:
                list.append(i)
                
                if n//i !=i:
                    list.append(n//i)
        return list
obj=Solution()
list=obj.print_all_divisors(22)
print(sorted(list))