import re

line = input()
t = int(line)

pattern = r'[a-z]'

while t > 0:
    ans = ''
    for i in range(8):
        line = input()
        ans += ''.join(re.findall(pattern, line))

    print(ans)

    t -= 1
