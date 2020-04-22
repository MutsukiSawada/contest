# ['表面', '南面', '東面', '西面', '北面', '裏面']
N = int(input())
dices = [[int(d) for d in input().split()] for _ in range(N)]

R1 = [
    [0, 1, 2, 3, 4, 5], # 移動なし
    [3, 1, 0, 5, 4, 2], # 東へ1
    [2, 1, 5, 0, 4, 3], # 西へ1
    [4, 0, 2, 3, 5, 1], # 南へ1
    [1, 5, 2, 3, 0, 4], # 北へ1
    [5, 4, 2, 3, 1, 0]  # 北へ2
]

R2 = [0, 3, 1, 4, 2, 5] # 水平回り1

ans = 'Yes'

for i in range(N):
    for j in range(i + 1, N):
        for r1 in R1:
            dice = [dices[j][k] for k in r1]
            for _ in range(4):
                dice = [dice[l] for l in R2]
                if dices[i] == dice:
                    ans = 'No'

print(ans)