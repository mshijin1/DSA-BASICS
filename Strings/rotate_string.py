# Vrute force approach
# def rotate_string(s, goal):
    
#     for i in range(len(s)):
#         substring=s[i:] + s[:i]
        
#         if substring==goal:
#             print("Number of rotation required: ", i)
#             return True
#     return False

# s="hello"
# goal="lohelx"
# result=rotate_string(s, goal)
# print(result)


# Optimised approach

def rotate_string(s, goal):
    combined_string=s+s
    return True if goal in combined_string else False

s="hello"
goal="lohelx"
result=rotate_string(s, goal)
print(result)