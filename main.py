def word_frequency(text):
    text = text.lower()
    for char in ",.!?":
        text = text.replace(char," ")
        words = text.split()
        freq = {}
    for word in words:
            freq[word] = freq.get(word, 0) + 1
    return freq
sentence = input("Enter a sentence: ")
result = word_frequency(sentence)
print("\nWord Frequency:")
for word, count in result.items():
    print(f"{word} :{count}")