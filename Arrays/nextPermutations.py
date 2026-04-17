# Brute Force approach
# from itertools import permutations

# perms= sorted(set(permutations([1,2,3])))

# current=tuple([3,2,1])
# print("current: " , current)

# # traverse the list

# for i in range(len(perms)):
#     if perms[i]==current:
#         if i==len(perms)-1:
#             print("Next permutation: ", perms[0])
#         else:
#             print("Next permutation: ", perms[i+1])
            
            
# Optimal Approach

def nextPermutation(nums):
    n=len(nums)
    breakpoint=-1
    
    for i in range(n-2, -1, -1):
        if nums[i]<nums[i+1]:
            breakpoint=i
            break
        
    # if no such breakpoint is found
    if breakpoint==-1:
        nums.reverse()
        return nums

    for j in range(n-1, breakpoint, -1):
        if nums[j]>breakpoint:
            # swap them
            nums[j], nums[breakpoint]=nums[breakpoint], nums[j]
            break
    
    # reverse the subarray from breakpoint+1 to end
    nums[breakpoint+1:]=reversed(nums[breakpoint+1:])
        

nums=[1,2,3]
nextPermutation(nums)

# Print result
print(" ".join(map(str, nums)))
# print("Next permutation: ", result)
