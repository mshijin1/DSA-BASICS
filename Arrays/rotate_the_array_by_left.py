def rotate_the_array(arr,k):
    while k!=0:
        first_element=arr[0]
        for i in range(1, len(arr)):
            arr[i-1]=arr[i]
            
        arr[len(arr)-1]=first_element
        k-=1
    # arr[len(arr)-1]=last_element
        
    print(arr)

arr=[1,2,3,4,5,6,7,8,9]
k=2
rotate_the_array(arr,k)