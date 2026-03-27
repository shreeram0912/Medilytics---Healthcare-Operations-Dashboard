def reverse_words(text):
    return ''.join(text[::-1]).split()[::-1]

text = "Hello World from Infosys"
print(reverse_words(text))