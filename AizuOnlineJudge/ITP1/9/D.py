STR = input()
Q = int(input())
for _ in range(Q):
    com = input().split()
    if com[0] == 'print':
        a, b = int(com[1]), int(com[2])
        print(STR[a:b + 1])
    if com[0] == 'reverse':
        a, b = int(com[1]), int(com[2])
        STR = STR[:a] + STR[a:b + 1][::-1] + STR[b + 1:]
    if com[0] == 'replace':
        a, b, alt = int(com[1]), int(com[2]), com[3]
        STR = STR[:a] + alt + STR[b + 1:]