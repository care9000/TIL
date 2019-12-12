import sys
sys.stdin = open('연구소.txt ')

def dfs(i, j):
    visited[i][j] = 1
    for k in range(4):
        i_test = i + i_move[k]
        j_test = j + j_move[k]
        if ispass(i_test, j_test):
            if data[i_test][j_test] == 0:
                dfs(i_test, j_test)




def check():
    global min_cnt
    for dd in range(len(vava)):
        dfs(vava[dd][0], vava[dd][1])
    cnt = 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] == 0 and data[i][j] == 0:
                cnt += 1
            elif visited[i][j] != 0:
                visited[i][j] = 0
    if min_cnt < cnt:
        min_cnt = cnt





def comb(n, r):
    if r == 0:
        for i in range(3):
            data[A[i][0]][A[i][1]] = 1
        check()
        for i in range(3):
            data[A[i][0]][A[i][1]] = 0

    elif n < r:
        return
    else:
        A[r-1] = info[n-1]
        comb(n - 1, r - 1)
        comb(n - 1, r)

def ispass(i, j):
    if 0 <= i < N and 0 <= j < M and visited[i][j] == 0:
        return True
    return False

i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
info = []
vava = []
visited = [[0 for _ in range(M)] for _ in range(N)]
min_cnt = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            info.append([i, j])
        elif data[i][j] == 2:
            vava.append([i, j])

A = [0] * 3
comb(len(info), 3)
print(min_cnt)