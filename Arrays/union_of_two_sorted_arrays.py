# # Using Map method
# def union_of_arrays(arr1, arr2):
#     n1=len(arr1)
#     n2=len(arr2)
#     freq={}
#     for i in range(n1):
#         freq[arr1[i]]=freq.get(arr1[i], 0) + 1
#     for j in range(n2):
#         freq[arr2[j]]=freq.get(arr2[j], 0) + 1
#     union=sorted(freq.keys())
    
#     return union

# arr1=[1,2,3,4]
# arr2=[0,3,4,5]
# result=union_of_arrays(arr1, arr2)
# print(result)

# Time = o(m+n)
# space o(m+n)

# Using Set

# Using Map method
# def union_of_arrays(arr1, arr2):
#     Set=set(arr1) | set(arr2)
#     union=sorted(Set)
    
#     return union

# arr1=[1,2,3,4]
# arr2=[0,3,4,5]
# result=union_of_arrays(arr1, arr2)
# print(result)


# Using two pointers approch
def union_of_arrays(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    union=[]
    
    while i<n1 and j<n2:
        if arr1[i] < arr2[j]:
            if not union or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            if not union or union[-1]!=arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
            
    return union

arr1=[1,2,3,4]
arr2=[0,3,4,5]
result=union_of_arrays(arr1, arr2)
print(result)