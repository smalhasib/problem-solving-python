from math import *

line = input()
T = int(line)

for t in range(T):
    line = input()
    a, b, L = map(int, line.split())

    lcm = (a * b) / gcd(a, b)

    if L % lcm == 0:
        prod = L / lcm
        _gcd = gcd(int(prod), int(lcm))
        while _gcd != 1.0:
            prod *= _gcd
            lcm /= _gcd
            _gcd = gcd(int(prod), int(lcm))
        print(f"Case {t + 1}: {int(prod)}")
    else:
        print(f"Case {t + 1}: impossible")
