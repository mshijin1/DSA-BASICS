# def subarray_with_xor_k(arr, k):
#     n=len(arr)
#     xor=0
#     xor_index={}
#     count=0
    
#     for i, val in enumerate(arr):
#         xor^=val
        
#         if xor==k:
#             count+=1
#         elif xor in xor_index:
#             count+=1
#         else:
#             xor_index[xor]=xor
    
#     return count

# arr=[4, 2, 2, 6, 4]
# k=6
# result=subarray_with_xor_k(arr, k)
# print("The number of subarrays with given xor k are: ", result)


# # brute force

# def subarray_with_xor_k(arr, k):
#     n=len(arr)
#     xor=0
#     xor_index={}
#     count=0
    
#     for i in range(n):
#         xor=0
#         for j in range(i, n):
#             xor^=arr[j]
            
#             if xor==k:
#                 count +=1
#     return count

# arr=[4, 2, 2, 6, 4]
# k=6
# result=subarray_with_xor_k(arr, k)
# print("The number of subarrays with given xor k are: ", result)


# Optimal approach

