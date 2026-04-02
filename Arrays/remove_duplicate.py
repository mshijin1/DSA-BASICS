def remove_duplicate(arr):
    unique=[]
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            unique.append(arr[i])
    return len(unique)            

arr=[1,2,3,3,4,5,5,6,6,6,7]
result=remove_duplicate(arr)
print(result)