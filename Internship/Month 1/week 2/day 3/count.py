def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

text = "hi hello!! this is infosys internship program."
print(word_frequency(text))
