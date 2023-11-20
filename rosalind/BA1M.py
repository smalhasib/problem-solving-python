val = int(input())
k = int(input())

seq = ['A', 'C', 'G', 'T']

ans = ''
for i in range(k):
    ans += seq[val % 4]
    val = val // 4

print(ans[::-1])
