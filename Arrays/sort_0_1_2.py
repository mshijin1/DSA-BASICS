def sort_the_given_array(arr):
    
    # point low and mid  to 0 and high to n-1
    mid=0
    low=0
    high=len(arr)-1
    
    while mid<=high:
        #if arr[mid] is zero than swap with element of low with element of mid and increase both low and mid
        if arr[mid]==0:
            swap(arr, low, mid)
            low+=1
            mid+=1
        # if arr[mid] is 1 than increase mide by 1 just that
        elif arr[mid]==1:
            mid+=1
        else:
            # else arr[mid] is 2 , swap the element of mid with th elemnet of high and decrease high by 1
            swap(arr, mid, high)
            high-=1
   
    return arr

# funtion to swap the elements
def swap(arr, i, j):
    arr[i], arr[j]=arr[j], arr[i]
    
    
arr=[0,1,2,0,1,2]
result=sort_the_given_array(arr)
print(result)