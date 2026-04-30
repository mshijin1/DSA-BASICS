def pascals_triangle(n):
    for row in range(1, n+1):
        c=1
        for i in range(1, row+1):
            print(c, end=" ")
            c=c*(row-i)//i
        print()

n=5
result=pascals_triangle(n)

# Time Complexity: O(n^2)
# Space Complexity: O(1)