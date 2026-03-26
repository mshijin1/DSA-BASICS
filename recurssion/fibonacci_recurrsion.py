def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        # print(fibonacci(n-1)+fibonacci(n-2), end=" | ")
        return fibonacci(n-1)+fibonacci(n-2)
    
result=fibonacci(int(input("Enter your number: ")))
print("Fibonacci of a number is: ", result)