# Brute force approch
# def two_sum(arr, target):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]+arr[j]==target:
#                 return i,j
# arr=[2,6,5,8,11]
# target=14
# result=two_sum(arr, target)
# print(result)


# Using map
def two_sum(arr, target):
    n=len(arr)
    map={}
    for i in range(n):
        diff=target-arr[i]
        if diff in map:
            return map[diff], i
        else:
            map[arr[i]]=i
    
    return "No such pair found"

arr=[2,6,5,10,11]
target=14
result=two_sum(arr, target)
print(result)
