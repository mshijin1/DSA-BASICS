# Brute force

# def largest_subarray_with_sum0(arr):
#     n=len(arr)
#     max_len=0
#     sum_index={}
#     sum=0
#     for i , val in enumerate(arr):
#         sum+=val 
#         if sum==0:
#             max_len=i+1  
#         elif sum in sum_index:
#             max_len=max(max_len, i-sum_index[sum])
#         else:
#             sum_index[sum]=i
#     return max
            
# arr=[9, -3, 3, -1, 6, -5]
# result=largest_subarray_with_sum0(arr)
# print("The length of the largest sub-array with sum zero is: ", result)


