def find_longest_consecutive_ones(arr):
    ones=0
    max_count=0
    n=len(arr)
    for i in range(n):
        if arr[i]==0:
            max_count=ones
            ones=0
        else:
            ones+=1
    return max_count

arr=[1, 1, 1, 1, 1, 0, 1, 1, 1]
result=find_longest_consecutive_ones(arr)
print(result)