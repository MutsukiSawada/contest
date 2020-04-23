import queue

N, Q = map(int, input().split())

P = queue.Queue()
for _ in range(N):
    p = input().split()
    P.put([p[0], int(p[1])])

time = 0
while not P.empty():
    p = P.get()
    if p[1] <= Q:
        time += p[1]
        print(p[0], time)
    else:
        time += Q
        P.put([p[0], p[1] - Q])