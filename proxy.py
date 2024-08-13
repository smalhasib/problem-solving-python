n = int(input())


def prec(c: str) -> int:
    if c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


result = []
stack = []

while n > 0:
    line = input()
    if line.strip() == '':
        while stack:
            result.append(stack.pop())
        print(''.join(result))

        n -= 1
        result = []
        stack = []
        continue

    if '0' <= line <= '9':
        result.append(line)
    elif line == '(':
        stack.append(line)
    elif line == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and (prec(line) < prec(stack[-1]) or
                         (prec(line) == prec(stack[-1]))):
            result.append(stack.pop())
        stack.append(line)
