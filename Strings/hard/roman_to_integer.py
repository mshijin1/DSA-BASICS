def roman_to_integer(s):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    sum=0
    for i in range(len(s)):
        if i < len(s) - 1 and eval(s[i]) < eval(s[i + 1]):
            sum -= eval(s[i])
        else:
            sum += eval(s[i])
    return sum
s="MCMXCIV"
result=roman_to_integer(s)
print(result)