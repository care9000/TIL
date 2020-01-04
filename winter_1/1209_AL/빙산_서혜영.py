import sys
sys.stdin = open('빙산.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def counting(i, j): # 빙산 옆 바다를 세서 저장
    Q = deque()
    Q.append([i, j])


    sea_info = [[0] * M for _ in range(N)]

    q = Q.popleft()
    sea = 0
    for z in range(4):
        nx = q[0] + dx[z]
        ny = q[1] + dy[z]
        if -1 < nx < N and -1 < ny < M:
            if ice[nx][ny] == 0:
                vis[nx][ny] = -1
                sea += 1
            elif ice[nx][ny] > 0 and vis[nx][ny] == 0:
                vis[nx][ny] = -1
                Q.append([nx, ny])

        sea_info[q[0]][q[1]] = sea

    melt(sea_info)

def melt(arr): # 녹이고
    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] > 0:
                ice[i][j] -= arr[i][j]
                if ice[i][j] <= 0:
                    ice[i][j] = 99



def check(arr): # 하나인지 확인
    global result, flag

    vis1 = [[0] * M for _ in range(N)]
    cnt1 = 0

    Q = deque()
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] > 0 and vis1[i][j] == 0:
                cnt1 += 1
                Q.append([i, j])
                vis1[i][j] = 9

                while Q:
                    q = Q.popleft()
                    for z in range(4):
                        nx = q[0] + dx[z]
                        ny = q[1] + dy[z]
                        if -1 < nx < N and -1 < ny < M:
                            if arr[nx][ny] > 0 and vis1[nx][ny] == 0:
                                Q.append([nx, ny])
                                vis1[nx][ny] = 9


    if cnt1 == 1: # 하나임..
        result += 1
        return
    # 여기 카운터가 2가아니라 2이상임..
    elif cnt1 >= 2:
        result += 1
        flag = 1
        return


N, M = map(int, input().split()) # 행, 열

ice = []
for i in range(N):
    ice.append(list(map(int, input().split())))

result = 0

flag = 0
# [print(ice[i]) for i in range(N)]
# print()
while not flag:
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] > 0:
                cnt += 1
                vis = [[0] * M for _ in range(N)]
                counting(i, j)

    #손댄부분 만약 아이스가 다녹으면 99로만들고 한꺼번에 녹임
    for i in range(N):
        for j in range(M):
            if ice[i][j] == 99:
                ice[i][j] = 0
    # 다녹인다음 빙산이 1덩어리 인지 2덩어리인지 확인
    check(ice)

    # flag == 1이면(두덩이 이므로) 출력!
    if flag == 1:
        break
    if cnt == 0:
        result = 0
        break
    # [print(ice[i]) for i in range(N)]
    # print()

print(result)