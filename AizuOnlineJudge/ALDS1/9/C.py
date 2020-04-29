from heapq import heappush, heappop

H = []
while True:
    com = input().split()
    if com[0] == 'insert':
        key = int(com[1])
        heappush(H, -key)
    elif com[0] == 'extract':
        print(-heappop(H))
    elif com[0] == 'end':
        break