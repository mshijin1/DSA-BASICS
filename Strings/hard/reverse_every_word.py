def reverse_every_word(s):
    result=""
    ans=[]
    for i in range(len(s)-1, -1, -1):
        if s[i]!=" ":
            result=s[i]+result
            print(result)
        else:
            ans.append(result)
            result=""
    ans.append(result)
    return ans

s="bungle in the jungle"
result=reverse_every_word(s)
print(result)