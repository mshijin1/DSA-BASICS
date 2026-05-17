def remove_outermost_paranthesis(s):
    open_count=0
    close_count=0
    result=""
    start=0
    
    for i , c in enumerate(s):
        if c=="(":
           open_count+=1
        elif c==")":
            close_count+=1
        
        if open_count==close_count: 
            result+=s[start+1:i]
            start=i+1
    return result 

s="()(()())(())"
print(remove_outermost_paranthesis(s))