def rotate_the_array_right(arr,k):
    n=len(arr)
    while k!=0:
        first_element=arr[n-1]
        for i in range(n, 1, -1):
            arr[i-1]=arr[i-2]
        arr[0]=first_element
        k-=1
    print(arr)

arr=[1,2,3,4,5,6,7,8,9]
k=3
mod=k % len(arr)
print(mod)
rotate_the_array_right(arr,k)