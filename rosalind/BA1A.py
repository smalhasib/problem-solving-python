text = input()
pattern = input()

cnt = sum(1 for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern)

print(cnt)
