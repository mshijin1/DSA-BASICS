def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break
    return arr

arr=[64,199, 25, 12, 22, 11]

print("Before bubble sort:")
print(*arr)
result=bubble_sort(arr)

print("After bubble sort:")
print(*result)