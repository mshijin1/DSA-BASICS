# Reversing using inbuild function
def reverse_array(arr):
    return arr[::-1]

result = reverse_array([1, 2, 3, 4, 5])
print("Reversing array using an inbuild function:", result)

# reversing using iteration
def reverse_array_iteration(arr):
    arr2 = [0] * len(arr)
    
    for i in range(len(arr2)):
        arr2[i]=arr[len(arr)-1-i]
    return arr2

result = reverse_array_iteration([1, 2, 3, 4, 5])
print("Reversing array using iteration:", result)