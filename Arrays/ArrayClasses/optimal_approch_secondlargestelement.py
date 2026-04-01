def find_second_largest(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    large=0
    second_large=0
    for i in range(len(arr)):
        if arr[i]>large:
            large=arr[i]
        if arr[i]<large and arr[i]>second_large:
            second_large=arr[i]
            
    return large, second_large
    

arr=[1,3,5,78,3,4,55]
result=find_second_largest(arr)
print(result)