def atoi(s):
    idx=0
    sign=1
    result=0
    
    for idx in range(len(s)):
        if s[idx]==" " or s[idx]=="+":
            continue
        elif s[idx]=="-":
            sign=-1
        elif s[idx].isdigit():
            result=result*10+int(s[idx])
        else:
            break
    return sign * result

s="  -0012g4"
result=atoi(s)
print(result)