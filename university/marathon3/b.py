line = input()
T = int(line)

for i in range(T):
    line = input()
    A, B, C = map(int, line.split())

    if C < A < B or B < A < C:
        print(A)
    elif A < C < B or B < C < A:
        print(C)
    elif A < B < C or C < B < A:
        print(B)
