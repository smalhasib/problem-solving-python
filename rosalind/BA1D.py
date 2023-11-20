pattern = input()
text = input()

positions = [i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern]

print(" ".join(map(str, positions)))
