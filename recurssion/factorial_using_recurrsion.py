class Solution:
    def factorial(self, num):
        return num * self.factorial(num-1) if num>=1 else 1

print(Solution().factorial(int(input("Enter a number: "))))