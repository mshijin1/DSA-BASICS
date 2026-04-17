def kadanes_Algorithm(arr):
    max_sum=arr[0]
    current_sum=0
    n=len(arr)
    i=0
    start=0
    anstart=-1
    anend=-1
    
    if i==n-1 and current_sum==0:
        return 0
    
    while i<n:
        current_sum+=arr[i]
        variable=arr[i]
        
        if current_sum==0:
            start=i
        
        if current_sum>max_sum:
            anstart=start
            anend=i
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
        i+=1
    
    for j in range(anstart, anend+1):
        print(arr[j], end=" ")
    
    return max_sum

arr=[2, 3, 5, -2, 7, -4] 
  
result=kadanes_Algorithm(arr)
print("Maximum sum found is ", result, end=" ")
            