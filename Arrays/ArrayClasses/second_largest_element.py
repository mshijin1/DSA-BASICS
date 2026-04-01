def find_second_largest(arr):
    i=0
    j=1
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            print("i-> ", i, "j-> ", j, "min_index-> ", min_index)
            if(arr[j]<arr[min_index]):
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    second_largest_element=arr[len(arr)-2]
    second_smallest_element=arr[1]
            
    return second_smallest_element, second_largest_element
            
arr=[1,7,0,4,9,6]
result=find_second_largest(arr)
print("second smallest element: ", result[0], " " , "Second largest element: ",result[1])