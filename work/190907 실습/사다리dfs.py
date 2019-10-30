import sys
sys.stdin = open('ladder2_input.txt')

def dfs(i, j):
    global a
    visited[i][j] = a

    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    for z in range(3):
        nx = i + dx[z]
        ny = j + dy[z]

        if -1 < nx < 100 and -1 < ny < 100:

            if ladder[nx][ny] == 1 and visited[nx][ny] == 0:
                a += 1
                dfs(nx, ny)

T = 10

for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    check = [0] * 100
    # 출발지 찾기

    for i in range(100):
        a = 1

        if ladder[0][i] == 1:
            visited = [[0] * 100 for _ in range(100)]

            dfs(0, i)

            min1 = 988765
            for j in range(100):
                if visited[99][j] != 0:
                    if visited[99][j] <= min1:
                        min1 = visited[99][j]

            check[i] = min1

        # for i in range(100):
        #     print(visited[i])

    min = 99878744
    min_idx = 0
    for k in range(100):
        if check[k] != 0:
            if check[k] <= min:
                min = check[k]
                min_idx = check.index(check[k])

    print('#{} {}'.format(tc, min_idx))