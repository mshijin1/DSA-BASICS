# All the occuranece of the same character shoud be in the same index
def isomorphic_string(s, t):
    m1={}
    m2={}
    
    for i in range(len(s)):
        if s[i] not in m1:
            m1[s[i]]=i
        if t[i] not in m2:
            m2[t[i]]=i
        if m1[s[i]]!=m2[t[i]]:
            return False
    return True

s="foo"
t="bar"
result=isomorphic_string(s,t)
print(result)

