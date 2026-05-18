
# Easist approach
def reverse_words_in_string(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

s="bungle in the jungle"
result=reverse_words_in_string(s)
print(result)