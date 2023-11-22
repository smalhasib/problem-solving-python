line = input()
T = int(line)

for t in range(T):
    line = input()
    students, lines = map(int, line.split())

    mappings = set()
    for i in range(lines):
        mappings.add(input())

    if len(mappings) == lines:
        print(f"Scenario #{t + 1}: possible")
    else:
        print(f"Scenario #{t + 1}: impossible")
