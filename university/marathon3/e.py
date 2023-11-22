line = input()
n = int(line)

for s in range(n):
    line = input()

    ans = False
    stack = []
    for i in line:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif stack:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                ans = True
        else:
            ans = True

    if ans:
        print("NO")
    elif stack:
        print("NO")
    else:
        print("YES")
