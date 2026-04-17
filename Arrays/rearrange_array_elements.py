# brute force approach
# def rearrange_array_elements_by_sign(arr):
#     n=len(arr)
#     positive=[]
#     negetive=[]
#     for i in range(n):
#         if arr[i]>=0:
#             positive.append(arr[i])
#         else:
#             negetive.append(arr[i])
            
#     for j in range(n//2):
#         arr[2*j]=positive[j]
#         arr[2*j+1]=negetive[j]
    
#     return arr

# arr=[1,2,-4,-5,7,8,-9,-2,-3, 10]
# result=rearrange_array_elements_by_sign(arr)
# print(result)


# optimum approach

def rearrange_array_elements_by_sign(arr):
    n=len(arr)
    positive_index=0
    negetive_index=1
    resultant_arr=[0] * n
    
    for i in range(n):
        if arr[i]>=0:
            resultant_arr[positive_index]=arr[i]
            positive_index+=2
        else:
            resultant_arr[negetive_index]=arr[i]
            negetive_index+=2
            
    return resultant_arr

arr=[1,2,-4,-5,7,8,-9,-2,-3, 10]
result=rearrange_array_elements_by_sign(arr)
print(result)