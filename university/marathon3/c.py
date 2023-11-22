def compare(item):
    return len(item), item


line = input()
n = int(line)

strings = [input() for i in range(n)]

strings.sort(key=compare)

ans = True
for i in range(len(strings) - 1):
    if strings[i] in strings[i + 1]:
        continue
    else:
        ans = False

if ans:
    print("YES")
    for i in strings:
        print(i)
else:
    print("NO")
