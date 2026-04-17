# Better Way
# def majority_element(arr):
#     n=len(arr)
#     limit=float(n//2)
#     freq={}
#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]]=1
    
#     for k, v in freq.items():
#         if v>=limit:
#             return k
    
#     return "Such number does not exist"

# arr=[2,2,1,1,1,2,2, 4,4,4,4,4,4,4,4,4,4]
# result=majority_element(arr)
# print(result)

# Optimised Way
def majority_element(arr):
    n=len(arr)
    limit=float(n//2)
    element=arr[0]
    count=0
    
    for i in range(n):
        if count==0 and arr[i]!=element:
            element=arr[i]
        if arr[i]==element:
            count+=1
        else:
            count-=1
    return element

arr=[2,2,1,1,1,2,2,4,4,4,4,4,4,4,4,4,4]
result=majority_element(arr)
print(result)