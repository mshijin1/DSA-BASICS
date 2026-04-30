# Brute force

# def four_sum(nums, target):
#     n=len(nums)
#     st=set()
    
#     if n==0 or n<4:
#         return nums
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                         temp=tuple(sorted([nums[i], nums[j] , nums[k] , nums[l]]))
#                         st.add(temp)
#      # Convert set to list of lists
#     return [list(quad) for quad in st]

# nums=[1,0,-1,0,-2,2]
# target=0
# result=four_sum(nums, target)
# print(" The combinations are: ", result)

# Optimised approach
def four_sum(nums, target):
    n=len(nums)
    nums.sort()
    ans=[]
    
    for first in range(n):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        
        for second in range(first+1, n):
            if second > first+1 and nums[second]==nums[second-1]:
                continue
        
            left, right=second+1, n-1
        
            while left<right:
            
                total= nums[first] + nums[second] + nums[left] + nums[right]
             
                if total == target:
                    ans.append([nums[first], nums[second], nums[left], nums[right]])
                 
                    while left < right and nums[left]==nums[left+1]:
                         left+=1
                    while left< right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
    return ans 
            
                    
nums=[4,3,3,4,4,2,1,2,1,1]
target=5
result=four_sum(nums, target)
print("The combinations are : ", result)
