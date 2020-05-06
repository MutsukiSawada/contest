# D - Caracal vs Monster

H = int(input())

def attack_cnt(h):
    if h == 1:
        return 1
    return 2 * attack_cnt(h // 2) + 1

print(attack_cnt(H))
