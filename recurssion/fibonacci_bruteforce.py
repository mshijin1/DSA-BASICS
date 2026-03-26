# Bruteforce approch
class Solution:
    i=0
    a=0
    b=1
    def fibonacci(self, n):
        print(self.a)
        print(self.b)
        while self.i<n-1:
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                c=self.a+self.b
                print(c)
                self.a=self.b
                self.b=c
                self.i+=1

Solution().fibonacci(int(input("Enter your number: ")))