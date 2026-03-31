def insertion_sort(arr, start, n):
    if start==n:
        return arr
    # key=arr[start]
    j=start
    
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1], arr[j]=arr[j], arr[j-1]
        j-=1
    
    return insertion_sort(arr, start+1, n)
            

arr=[64, 199, 25, 12, 22, 11]
print("Before insertion sort:")
print(*arr)
n=len(arr)
result=insertion_sort(arr, 0, n)
print("After insertion sort:")
print(result)