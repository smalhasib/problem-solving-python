from sys import stdin, stdout

line = stdin.readline().split()[0]
n = int(line)

count = {}
mx = 1000000
for i in range(n):
    words = stdin.readline().split()

    code = (words[0], words[1])
    count[code] = words[2]

line = stdin.readline().split()[0]
t = int(line)

for i in range(t):
    words = stdin.readline().split()
    code = (words[0], words[1])

    stdout.write(f'{count[code]}\n')
