import sys
sys.stdin = open('섬_input.txt')

def dfs(x, y):

    visited[x][y] = 1

    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]

    for z in range(8):
        new_x = x + dx[z]
        new_y = y + dy[z]
        if -1 < new_x < N and -1 < new_y < N:
            if arr[new_x][new_y] >= 1 and visited[new_x][new_y] == 0:
                dfs(new_x, new_y)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print('#{} {}'.format(tc, cnt))
