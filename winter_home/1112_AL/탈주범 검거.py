import sys
sys.stdin = open('탈주범 검거.txt')
def bfs(i, j):
    q = []
    q.append((i, j, 1))
    rr = 0
    while len(q) != rr:
        a = q[rr]
        i_tem = a[0]
        j_tem = a[1]
        vis[i_tem][j_tem] = 1
        if a[2] < L:
            if data[i_tem][j_tem] == 1:
                for k in range(4):
                    i_test = i_tem + i_move_1[k]
                    j_test = j_tem + j_move_1[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 2:
                            if data[i_test][j_test] == 2 or data[i_test][j_test] == 5 or data[i_test][j_test] == 1 or data[i_test][j_test] == 6:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 4 or data[i_test][j_test] ==5:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 6 or data[i_test][j_test] ==7:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 3:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 2 or data[i_test][j_test] == 4 or data[i_test][j_test] ==7:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 2:
                for k in range(2):
                    i_test = i_tem + i_move_2[k]
                    j_test = j_tem + j_move_2[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 0:
                            if data[i_test][j_test] == 5 or data[i_test][j_test] == 6 or data[i_test][j_test] == 1 or data[i_test][j_test] == 2:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] ==4 or data[i_test][j_test] ==7 or data[i_test][j_test] == 1 or data[i_test][j_test] == 2:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 3:
                for k in range(2):
                    i_test = i_tem + i_move_3[k]
                    j_test = j_tem + j_move_3[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] ==5 or data[i_test][j_test] == 4:
                                q.append((i_test, j_test, a[2] + 1))
                        if k == 1:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 6 or data[i_test][j_test] == 7:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 4:
                for k in range(2):
                    i_test = i_tem + i_move_4[k]
                    j_test = j_tem + j_move_4[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 2 or data[i_test][j_test] == 5 or data[i_test][j_test] == 6:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] ==1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 6 or data[i_test][j_test] == 7:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 5:
                for k in range(2):
                    i_test = i_tem + i_move_5[k]
                    j_test = j_tem + j_move_5[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 2 or data[i_test][j_test] == 4 or data[i_test][j_test] == 7:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 6 or data[i_test][j_test] == 7:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 6:
                for k in range(2):
                    i_test = i_tem + i_move_6[k]
                    j_test = j_tem + j_move_6[k]
                    if ispass(i_test, j_test) and vis[i_test][j_test] == 0:
                        if k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 5 or data[i_test][j_test] == 4:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 2 or data[i_test][j_test] == 4 or data[i_test][j_test] == 7:
                                q.append((i_test, j_test, a[2] + 1))
            elif data[i_tem][j_tem] == 7 and vis[i_test][j_test] == 0:
                for k in range(2):
                    i_test = i_tem + i_move_7[k]
                    j_test = j_tem + j_move_7[k]
                    if ispass(i_test, j_test):
                        if k == 0:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 2 or data[i_test][j_test] == 5 or data[i_test][j_test] == 6:
                                q.append((i_test, j_test, a[2] + 1))
                        elif k == 1:
                            if data[i_test][j_test] == 1 or data[i_test][j_test] == 3 or data[i_test][j_test] == 4 or data[i_test][j_test] == 5:
                                q.append((i_test, j_test, a[2] + 1))
        rr += 1
def ispass(i, j):
    if 0 <= i < N and 0 <= j < M and data[i][j] != 0:
        return True
    return False


i_move_1 = [0, 0, -1, 1]
j_move_1 = [-1, 1, 0, 0]

i_move_2 = [-1, 1]
j_move_2 = [0, 0]

i_move_3 = [0, 0]
j_move_3 = [-1, 1]

i_move_4 = [-1, 0]
j_move_4 = [0, 1]

i_move_5 = [1, 0]
j_move_5 = [0, 1]

i_move_6 = [0, 1]
j_move_6 = [-1, 0]

i_move_7 = [-1, 0]
j_move_7 = [0, -1]


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0 for _ in range(M)] for _ in range(N)]
    bfs(R,C)
    cnt = 0
    for i in range(len(vis)):
        for j in range(len(vis[i])):
            if vis[i][j] == 1:
                cnt += 1
    print("#{} {}".format(tc, cnt))