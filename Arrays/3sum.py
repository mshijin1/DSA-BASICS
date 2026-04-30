# brute force

# def three_sum(nums):
#     n=len(nums)
#     st=set()
#     if n==3 or n<3:
#         return nums
        
#     for i in nums:
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     triplet=tuple(sorted([nums[i],  nums[j], nums[k]]))
#                     st.add(triplet)
#     # convert set to list
#     return [list(triplet) for triplet in st]

# nums=[-1, 0, 1, 2, -1, -4]
# result=three_sum(nums)
# print("combinations causing 0: ", result)


# Better approach
def three_sum(nums):
    nums.sort()
    n=len(nums)
    ans=[]
    # FIrst loop for the first number
    for i in range(n):
        # Skip duplicates for the first number
        if n>0 and nums[i] == nums[i-1]:
            continue
        
        # two pointer
        left, right=i+1, n-1
        
        # find pairs of current nums[i]
        while left<right:
            total=nums[i] + nums[left] + nums[right]
            
            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
            
                # Skip duplicates for left
                while left < right and nums[left]==nums[left-1]:
                    left+=1
                while left < right and nums[right]==nums[right+1]:
                    right-=1
            
            elif total<0:
                left+=1
            else:
                right-=1
    return ans

nums=[-1, 0, 1, 2, -1, -4]
result=three_sum(nums)
print("the combnations are: ", result)
