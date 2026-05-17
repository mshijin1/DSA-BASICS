def sort_character_by_frequency(s):
    freq=[0]*26
    
    for char in s:
        freq[ord(char)-ord('a')]+=1
    
    vec=[]
    for i in range(26):
        if freq[i]>0:
            vec.append((freq[i], chr(i+ord('a'))))
    
    ans=""
    for freq, char in vec:
        ans+=char*freq
    return set(ans)
s="tree"
result=sort_character_by_frequency(s)
print(result)