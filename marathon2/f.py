# fastest io in python
from sys import stdin, stdout

t = stdin.readline().split()[0]
t = int(t)

while t > 0:
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)

    if a % b == 0 or b % a == 0:
        stdout.write("true\n")
    else:
        stdout.write("false\n")
    t -= 1
