# TLE

H = []

def max_heapfiy(i):
    left = 2 * i
    right = 2 * i + 1
    if left <= len(H) and H[i - 1] < H[left - 1]:
        largest = left
    else:
        largest = i
    if right <= len(H) and H[largest - 1] < H[right - 1]:
        largest = right
    if largest != i:
        H[i - 1], H[largest - 1] = H[largest - 1], H[i - 1]
        max_heapfiy(largest)

def insert_node(key):
    H.append(key)
    i = len(H)
    while 1 < i and H[(i // 2) - 1] < H[i - 1]:
        H[i - 1], H[(i // 2) - 1] = H[(i // 2) - 1], H[i - 1]
        i = i // 2

def extract_node():
    i = len(H)
    if i < 1:
        return
    print(H[0])
    H[0] = H.pop()
    max_heapfiy(1)

while True:
    com = input().split()
    if com[0] == 'insert':
        key = int(com[1])
        insert_node(key)
    elif com[0] == 'extract':
        extract_node()
    elif com[0] == 'end':
        break