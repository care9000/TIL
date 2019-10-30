import sys
sys.stdin = open('미로_input.txt')

T = int(input())


def dfs(x, y):

    visited[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for z in range(4):
        new_x = x + dx[z]
        new_y = y + dy[z]
        if -1 < new_x < N and -1 < new_y < N:
            if data[new_x][new_y] == '0' and visited[new_x][new_y] == 0:
                dfs(new_x, new_y)
            elif data[new_x][new_y] == '3' and visited[new_x][new_y] == 0:
                dfs(new_x, new_y)



for tc in range(1, T+1):
    N = int(input())

    data = []
    visited = [[0] * N for _ in range(N)]
    flag = 0

    for _ in range(N):
        a = input()
        data.append(a)
    # print(data)

    for i in range(N):
        for j in range(N):
            if data[i][j] == '2' and visited[i][j] == 0:
                dfs(i, j)

    for i in range(N):
        for j in range(N):
            if data[i][j] == '3' and visited[i][j] == 1:
                flag = 1

    print('#{} {}'.format(tc, flag))