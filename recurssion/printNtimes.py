class Solution:
    def print_n_times(self, n):
        if n==0:
            return 1
        # print(n)
        return n * self.print_n_times(n-1)

obj=Solution()
result=obj.print_n_times(5)
print(result)

