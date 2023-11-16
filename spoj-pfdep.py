v = []
vis = list(False for i in range(101))

temp = input().split(' ')
n, m = [int(x) for x in temp]

for i in range(m):
    temp = input().split(' ')
    temp = [int(x) for x in temp]
    