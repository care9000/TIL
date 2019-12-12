def dfs(attack_scv, cnt):
    global min_cnt
    if cnt > min_cnt:
        return
    flag = 0
    for a in range(len(scv_hp)):
        if scv_hp[a] > 0:
            flag = 1
            break
    if flag == 0:
        if min_cnt > cnt:
            min_cnt = cnt
            return
    print(scv_hp, cnt)
    cnt += 1
    if scv_hp[attack_scv] > 0:
        scv_hp[attack_scv] -= 9
        for j in range(len(scv_hp)):
            if j != attack_scv and scv_hp[j] > 0:
                scv_hp[j] -= 3
                for k in range(len(scv_hp)):
                    if k != j and k != attack_scv and scv_hp[k] > 0:
                        scv_hp[k] -= 1
                        for l in range(len(scv_hp)):
                            if scv_hp[l] > 0:
                                dfs(l, cnt)
                        scv_hp[k] += 1
                scv_hp[j] += 3
        scv_hp[attack_scv] += 9




# scv 마리
N = input(int())
# 각 scv 체력
scv_hp = list(map(int, input().split()))
min_cnt = 987654321
for i in range(len(scv_hp)):
    dfs(i, 0)
print(min_cnt)
