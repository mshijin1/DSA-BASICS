def find_leader_in_an_array(arr):
    leader=[]
    max=arr[-1]
    leader.append(max)
    for i in range(len(arr)-2, -1, -1):
        if arr[i]>max:
            leader.append(arr[i])
            max=arr[i]
    
    return leader[::-1]

arr=[16,17,4,3,5,2]
arr2=[4, 7, 1, 0]
arr3=[10, 22, 12, 3, 0, 6]  
result= find_leader_in_an_array(arr)
print("Leaders in the array: ", result)