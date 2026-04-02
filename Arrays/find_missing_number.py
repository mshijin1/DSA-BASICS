# Using sum function

# def find_missing_number(arr):
#     n=len(arr)+1
#     sum1=0
#     for i in range(0,n-1):
#         sum1+=arr[i]
    
#     expected_sum=n * (n+1) // 2
     
#     total = expected_sum - sum1   
#     return total
    
# arr=[1,2,3,5,6,7]
# result=find_missing_number(arr)
# print(result)

# Using XOR

def find_missing_number(arr):
    n=len(arr)+1
    xor1=0
    xor2=0
    
    for i in range(0, n-1):
        xor1^=arr[i]
    for j in range(1, n+1):
        xor2^=j
        
    return xor1 ^ xor2
    
arr=[1,2,3,5,6,7]
result=find_missing_number(arr)
print(result)