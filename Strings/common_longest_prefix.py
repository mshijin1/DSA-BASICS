# brute force approach

# def common_longest_prefix(s):
#     # sort the array of string
#     s.sort()
    
#     # first and the last element of the sorted string
#     first=s[0]
#     last=s[-1]
    
#     minLen=min(len(first), len(last))
    
#     i=0
#     while i<minLen and first[i]==last[i]:
#         i+=1
        
    
#     return first[:i]

# s=["flower","flow","flight"]
# result=common_longest_prefix(s)
# print(result)

# Optimised approach

def commonPrefixUtil(s1, s2):
    res = []
    n1, n2 = len(s1), len(s2)

    for i in range(min(n1, n2)):
        if s1[i] != s2[i]:
            break
        res.append(s1[i])
  
    return ''.join(res)


def common_longest_prefix(s, start, end):
    
    if start==end:
        return s[start]
    
    if start<end:
        mid=(start+end)//2
        
        left=common_longest_prefix(s, start, mid)
        right=common_longest_prefix(s, mid+1, end)
        
        return commonPrefixUtil(left, right)
    

s=["geeksforgeeks", "geeks", "geek", "geezer"]
result=common_longest_prefix(s, 0, len(s)-1)
print(result)