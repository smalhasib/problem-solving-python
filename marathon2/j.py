line = input()
n, m = map(int, line.split())

name_of_ips = dict()
for i in range(n):
    line = input()
    name, ip = line.split()
    name_of_ips[ip] = name

for i in range(m):
    line = input()
    ip = line.split()[1][:-1]
    print(f"{line} #{name_of_ips[ip]}")
