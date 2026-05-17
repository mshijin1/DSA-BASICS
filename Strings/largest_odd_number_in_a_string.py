def largest_odd_number_in_a_string(s):
    length=len(s)
    for i in range(length-1,-1, -1):
        if int(s[i])%2!=0:
            return s[:i+1]

s="5047654"
result=largest_odd_number_in_a_string(s)
print(result)