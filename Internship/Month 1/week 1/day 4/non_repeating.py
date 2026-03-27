def non_repeat(s):
    for char in s:
        if s.count(char) == 1:
            return char
        return None
    
text1 = "hello"
text2 = "bye"
print(non_repeat(text1))
print(non_repeat(text2))