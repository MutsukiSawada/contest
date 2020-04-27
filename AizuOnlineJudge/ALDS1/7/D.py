N = int(input())
PRE = [int(i) for i in input().split()]
IN = [int(i) for i in input().split()]
POST = []
pos = 0

def rec(left, right):
    global pos
    if right <= left:
        return
    root = PRE[pos]
    pos += 1
    mid = IN.index(root)
    rec(left, mid)
    rec(mid + 1, right)
    POST.append(root)

rec(0, N)
print(*POST)