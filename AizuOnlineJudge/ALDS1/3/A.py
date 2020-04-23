stack = []
for s in input().split():
    if s.isdecimal():
        stack.append(int(s))
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(str(b) + s + str(a)))

print(stack[0])