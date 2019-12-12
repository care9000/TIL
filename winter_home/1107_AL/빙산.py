import sys
sys.stdin = open('빙산.txt')

def dfs(i, j):
    cnt = 0
    for k in range(4):
        i_test = i + i_move[k]
        j_test = j + j_move[k]
        if ispass(i_test, j_test):
            if data[i_test][j_test] == 0:
                cnt += 1
    data[i][j] -= cnt
    if data[i][j] <= 0:
        data[i][j] = 9999
        aa.append([i, j])

def check(i, j):
    q = []
    visited[i][j] = 1
    q.append((i, j))
    zz = 0
    while len(q) != zz:
        a = q[zz]
        i_tem = a[0]
        j_tem = a[1]
        for k in range(4):
            i_test = i_tem + i_move[k]
            j_test = j_tem + j_move[k]
            if ispass(i_test, j_test):
                if data[i_test][j_test] != 0 and visited[i_test][j_test] == 0:
                    visited[i_test][j_test] = 1
                    q.append((i_test, j_test))
        zz += 1


def ispass(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    return False

i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

year = 0
flag = 0
aaa = 0
ice = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            ice += 1
if ice == 0:
    aaa = 1
while ice != 0:
    aa = []
    year += 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                dfs(i, j)
    for i in range(len(aa)):
        data[aa[i][0]][aa[i][1]] = 0
        ice -= 1
    cnt = 0
    if ice == 0:
        aaa = 1
        break
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                if cnt != 1:
                    flag = 1
                    break
                check(i, j)
        if flag == 1:
            break
    if flag == 1:
        break

if aaa == 1:
    print(0)
else:
    print(year)
