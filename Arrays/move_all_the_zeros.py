# def move_all_the_zeros(arr):
#     n=len(arr)
#     pointer=0
#     zero=0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[pointer]=arr[i]
#             pointer+=1
#     for j in range(pointer, n):
#         arr[j]=0
        
#     return arr

# arr=[1,0,2,3,0,4,0,1]
# result=move_all_the_zeros(arr)  
# print(result)  


def move_all_the_zeros(arr):
    n=len(arr)
    pointer=0
    for i in range(n):
        if arr[i]!=0:
            arr[pointer], arr[i]=arr[i], arr[pointer]
            pointer+=1
        
    return arr

arr=[1,0,2,3,0,4,0,1]
result=move_all_the_zeros(arr)  
print(result) 