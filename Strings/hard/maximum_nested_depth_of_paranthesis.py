def maximium_nested_depth_of_paranthesis(s):
    current_depth=0
    max_depth=0
    for i in range(len(s)):
        if s[i]=="(":
            current_depth+=1
            max_depth=max(max_depth, current_depth)
        elif s[i]==")":
            current_depth-=1
    return max_depth
    
s="(1+(2*3)+((8)/4))+1"
result=maximium_nested_depth_of_paranthesis(s)
print(result)