# using frequency dictionary
# def single_digits(arr):
#     n=len(arr)
#     freq={}
#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]]=1
            
#     single_digit=freq
#     return [k for k, v in freq.items() if v==1]

# arr=[4, 4,2,1,2]
# result=single_digits(arr)
# print(result)

# Using XOR operator
def single_digits(arr):
    n=len(arr)
    xor=0
    for i in range(n):
        xor^=arr[i]
    
    return xor

arr=[4,2,1,2,1]
result=single_digits(arr)
print(result)