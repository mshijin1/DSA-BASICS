# brute force approach
# def anagrams_of_string(input1, input2):
    
#     if len(input1)!=len(input2):
#         return False
    
#     if sorted(input1)!=sorted(input2):
#         return False
#     return True 

# input1="RULES"
# input2="LESRT"
# result=anagrams_of_string(input1, input2)
# print(result)


# optimised approach
def anagrams_of_string(input1, input2):
    
    if len(input1)!=len(input2):
        return False
    
    freq=[0]*26
    
    for char in input1:
        freq[ord(char)-ord('A')]+=1
    for char in  input2:
        freq[ord(char)-ord('A')]-=1
        
    for count in freq:
        if count!=0:
            return False
    return True 

input1="CAT"
input2="ACT"
result=anagrams_of_string(input1, input2)
print(result)