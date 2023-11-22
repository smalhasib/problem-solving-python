line = input()
n, m = map(int, line.split())

line = input()
values_of_problems = list(map(int, line.split()))

line = input()
solved_problems = list(map(int, line.split()))

sum = 0
for i in solved_problems:
    sum += values_of_problems[i-1]

print(sum)
