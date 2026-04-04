def longest_subarray_with_given_k(arr, k):
    n=len(arr)
    max_sum=0
    max_length=0
    # loop from 0 to n
    for i in range(n-1):
        sum=0
        if i==len(arr)-1 and sum==0:
            return 0
        # loop from 1 to n
        for j in range(i+1, n):
            sum+=arr[j]
            
            if sum>k:
                break
            if sum==k:
                max_sum=sum
                max_length=j-i
                sum=0
    return max_length
            

arr=[-3, 2, 1]
k=6
result=longest_subarray_with_given_k(arr, k)
print(result)