a, op, b = 0, '', 0
while op != '?':
    a, op, b = input().split()
    if op == '+':
        print(int(a) + int(b))
    if op == '-':
        print(int(a) - int(b))
    if op == '*':
        print(int(a) * int(b))
    if op == '/':
        print(int(a) // int(b))