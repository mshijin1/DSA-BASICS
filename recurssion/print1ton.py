class Solution:
    def print_1_to_n(self, curr, n):
        if curr>n:
            return
        print(curr)
        self.print_1_to_n(curr+1, n)
    
obj=Solution()
num=5
obj.print_1_to_n(1, 1)