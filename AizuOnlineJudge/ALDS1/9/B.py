N = int(input())
H = [int(h) for h in input().split()]

def max_heapfiy(i):
    left = 2 * i
    right = 2 * i + 1
    if left <= N and H[i - 1] < H[left - 1]:
        largest = left
    else:
        largest = i
    if right <= N and H[largest - 1] < H[right - 1]:
        largest = right
    if largest != i:
        H[i - 1], H[largest - 1] = H[largest - 1], H[i - 1]
        max_heapfiy(largest)

for i in reversed(range(1, N // 2 + 1)):
    max_heapfiy(i)

print('', *H)