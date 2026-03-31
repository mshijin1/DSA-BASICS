def merge(arr, low, mid, high):
    temp=[]
    left=low
    right=mid+1
    
    # Merge both sorted halves
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
            
    # merge what is left from the left array
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
        
    for i in range(low, high + 1):
        arr[i]=temp[i - low]
        print(i, temp[i-low])

def merge_sort(arr, start, end):
    if start>=end:
        return
    # print(arr,start, end)
    mid=(start+end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr,start,mid,end)
        
arr=[64, 199, 25, 12, 22, 11]
# arr=[64]

result=merge_sort(arr,0,len(arr)-1)
print(arr)