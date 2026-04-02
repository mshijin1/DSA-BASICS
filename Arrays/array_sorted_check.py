def check_array_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
        
arr=[1,2,3,575,6,7,8,9]
result=check_array_sorted(arr)
print(result)