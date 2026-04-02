def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i]==element:
            return f"Element Found at {i}"

arr=[5,4,3,2,1]
element=5
result=linear_search(arr, element)
print(result)