# D - Lunlun Number

import queue

K = int(input())

Q = queue.Queue()
for i in range(1, 10):
    Q.put(i)
ans = 0
for _ in range(K):
    ans = Q.get()
    if ans % 10 != 0:
        Q.put((10 * ans) + (ans % 10) - 1)
    Q.put((10 * ans) + (ans % 10))
    if ans % 10 != 9:
        Q.put((10 * ans) + (ans % 10) + 1)

print(ans)