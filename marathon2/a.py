from sys import stdin, stdout
from math import gcd, sqrt

n, m, l, r = stdin.readline().split()
n = int(n)
m = int(m)
l = int(l)
r = int(r)

lcm = (n * m) // gcd(n, m)

res = 0
if l % lcm == 0:
    res = (r // lcm) - (l // lcm) + 1
else:
    res = (r // lcm) - (l // lcm)

stdout.write(f'{res}\n')
