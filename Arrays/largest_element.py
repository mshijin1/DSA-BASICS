def find_largest(arr):
    max=0
    for i in range(len(arr)):
        if arr[i]>=max:
            max=arr[i]
    return max

arr=[1, 2, 3, 14, 5, 6]
result=find_largest(arr)
print("The largest element is: ", result)