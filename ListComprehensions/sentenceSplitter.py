sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lenghts = []

for word in words:
    if word != "the":
        word_lenghts.append(len(word))

print(words)
print(word_lenghts)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)