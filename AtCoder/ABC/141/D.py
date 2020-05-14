# D - Powerful Discount Tickets

import heapq

N, M = map(int, input().split())
A = [int(a) * -1 for a in input().split()]
heapq.heapify(A)

for i in range(M):
    price = heapq.heappop(A)
    price = -1 * ((-1 * price) // 2)
    heapq.heappush(A, price)

print(sum(A) * -1)
