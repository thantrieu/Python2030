names = "I Love Learning Python At Branium Academy"
other = "How are you today"
words = names.split()
words.sort(key=lambda x: len(x), reverse=True)
print(words)
