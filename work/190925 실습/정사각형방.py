import sys
sys.stdin = open('정사각형방_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global cnt
    cnt += 1
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if -1 < nx < N and -1 < ny < N:
            if data[nx][ny] == data[x][y] + 1:
                dfs(nx, ny)
    #             if ret > max:
    #                 max = ret
    # return max + 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # print(data)
    
    start_val = (N*N)+1 #방번호
    max_cnt = 0 #이동수

    for i in range(N):
        for j in range(N):
            cnt = 0
            if data[i][j] <= (N**2) - max_cnt:
                dfs(i, j) # i, j 방 인덱스
                if cnt > max_cnt:
                    max_cnt = cnt
                    start_val = data[i][j]
                elif cnt == max_cnt:
                    if start_val > data[i][j]:
                        start_val = data[i][j]

    print('#{} {} {}'.format(tc, start_val, max_cnt))
