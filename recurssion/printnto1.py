class Solution:
    def print_n_to_1(self, num):
        if num==0:
            return
        print(num)
        self.print_n_to_1(num-1)
    
obj=Solution()
num=5
obj.print_n_to_1(num)