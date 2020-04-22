W = input().lower()
T = []
while True:
    t = input()
    if t == 'END_OF_TEXT':
        break
    T += t.lower().split()

print(T.count(W))