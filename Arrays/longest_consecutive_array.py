# Bruteforce approach 

# def linearSearch(nums, num):
#     n=len(nums)
    
#     for i in range(n):
#         if nums[i]==num:
#             return True
#     return False


# def find_the_longest_consecutive_array(nums):
#     n=len(nums)
#     longest=1
    
#     if n==0:
#         return 0
    
#     for i in range(n):
#         # current element
#         current=nums[i]
#         count=1
        
#         while linearSearch(nums, current+1):
#             current+=1
#             count+=1
        
#         longest=max(longest, count)
    
#     return longest
        
# nums=[100, 4, 200, 1, 3, 2]
# result=find_the_longest_consecutive_array(nums)
# print("Longest consecutive array: ", result)


# Optimal approach

# def sort_the_array(nums):
#     n=len(nums)
#     i=0
#     while i<=n:
#         for j in range(i+1, n):
#             if nums[j]<nums[i]:
#                 nums[j], nums[i]=nums[i], nums[j]
#         i+=1
#     return nums
        
        
# def find_the_longest_consecutive_array(nums):
#     n=len(nums)
#     longest=1
#     max_length=0
    
#     if n==0:
#         return 0
#     sorted_nums=sort_the_array(nums)
    
#     print("Sorted_nums: ", sorted_nums)
    
#     for i in range(1,n):
#         if nums[i-1]+1==nums[i]:
#             longest+=1
#             max_length = max(longest, max_length)
#         else:
#             longest=1
            
#     return max_length


# nums=[100, 4, 200, 1, 3, 2]
# result=find_the_longest_consecutive_array(nums)
# print("The length of the longest consecutive array is: ", result)


# Optimal approach using a set



def find_the_longest_consecutive_array(nums):
    n=len(nums)
    longest =1
    st=set()
    count=0
    # Storing all the elemets onto a set
    for i in range(n):
        st.add(nums[i])
        
    for element in st:
        # if the lement is the starting point of the sequence
        if element-1 not in st:
            # initialize the counter with the current scequence
            count=1
            
            # Starting element of the sequence
            x=element
            
            # Find the consecutive number
            while x+1 in st:
                # Move to the next element
                x=x+1
                
                # Increment the counter of the sequence
                count+=1
            
            # find the longest
            longest=max(longest, count)
            
    return longest
            
nums=[100, 4, 200, 1, 3, 2]
result=find_the_longest_consecutive_array(nums)
print("The length of the longest consecutive array is: ", result)
