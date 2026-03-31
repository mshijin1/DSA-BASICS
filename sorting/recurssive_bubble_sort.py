def bubble_sort(arr, n):
    if n==0:
        return
    swapped = False
        
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
            
    if not swapped:
        return
    
    bubble_sort(arr, n-1)
        
    return arr

arr=[64,199, 25, 12, 22, 11]

print("Before bubble sort:")
print(*arr)
n=len(arr)
result=bubble_sort(arr, n)

print("After bubble sort:")
print(*result)