# def Count_Subarray_Sum_Equals_k(nums, k):
#     i=0
#     j=0
#     count=0
#     current_sum=0
#     n=len(nums)
    
#     if n==0:
#         return "There is no eleents in the array"
#     if n==1:
#         return nums

#     while i<=j and j<n:
#         current_sum+=nums[j]
#         if current_sum==k:
#             count+=1
#             current_sum=0
#             i+=1
#             j=i
#         elif current_sum>k:
#             current_sum=0
#             i+=1
#             j=i
#         else:
#             j+=1
            
#     return count        
            
# nums=[1,2,3]
# k=3
# result=Count_Subarray_Sum_Equals_k(nums, k)

# print("The number  of subarrys whos sum = k : ", result)


# Optimal Solution
def Count_Subarray_Sum_Equals_k(nums, k):
    # Size of the array
    n=len(nums)
    # Dictionary to store the sum of the prefix sum
    prefixSumCount={}
    # Initialize prefixsm and count to 0
    prefixSum=0
    count=0
    # Base case prefix sum 0 has occured once
    prefixSumCount[0]=1

    # Traverse through the array
    for i in range(n):
        # Adding elements to the prefixSum
        prefixSum+=nums[i]
        # calculating the sum to be removed
        remove=prefixSum-k
        
        # If this prefix sum is seen before then add its count
        if remove in prefixSumCount:
            count+=prefixSumCount[remove]
        # Update the frequency of the current prefixSum
        prefixSumCount[prefixSum]=prefixSumCount.get(prefixSum, 0) + 1
        
    return count
        
# Main Function
nums=[3, 1, 2, 4]
k=6
result=Count_Subarray_Sum_Equals_k(nums, k)
print("The number of subarray is: ", result)

# Time Complexity: O(n)
# Space Complexity: O(n)