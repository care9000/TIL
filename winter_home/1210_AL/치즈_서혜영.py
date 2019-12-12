import sys
sys.stdin = open('치즈_input.txt')
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_b(x, y):
    Q = deque()
    Q.append([x, y])
    boundary[x][y] = 9

    while Q:
        q = Q.popleft()
        for z in range(4):
            nx = q[0] + dx[z]
            ny = q[1] + dy[z]
            if -1 < nx < N and -1 < ny < M:
                if cheeze[nx][ny] == 0 and boundary[nx][ny] == 0:
                    boundary[nx][ny] = 9
                    Q.append([nx, ny])
                elif cheeze[nx][ny] == 0 and boundary[nx][ny] == 9:
                    continue

def melt():
    for i in range(N):
        for j in range(M):
            flag = 0
            if cheeze[i][j] == 1:
                for z in range(4):
                    ni = i + dx[z]
                    nj = j + dy[z]
                    if -1 < ni < N and -1 < nj < M:
                        if boundary[ni][nj] == 9:
                            flag += 1
                if flag > 0:
                    cheeze[i][j] = 0

def is_final():
    temp_cnt = 0
    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 1:
                temp_cnt += 1

    return temp_cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 가로, 세로
    cheeze = []

    for _ in range(N):
        cheeze.append(list(map(int, input().split())))

    cheeze_by_time = []

    a = 1

    if not is_final():
        print(len(cheeze_by_time))
        print('0')

    else:
        while a:
            boundary = [[0] * M for _ in range(N)]
            find_b(0, 0)
            melt()
            a = is_final()
            cheeze_by_time.append(a)

        # print(cheeze_by_time)
        print(len(cheeze_by_time))
        print(cheeze_by_time[-1])