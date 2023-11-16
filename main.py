with open('rosalind_ba2c.txt', 'r') as file:
    pep = file.readline().strip()
    num = int(file.readline().strip())
    lines = [list(map(float, file.readline().split())) for i in range(4)]
    print(pep)
    print(num)
    print(lines)

print(format(3.1, '.4f'))
