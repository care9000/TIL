import sys
sys.stdin = open('미로_input.txt')

T = int(input())

def bfs(x, y):
    Q = []
    Q.append([x, y])
    visited[x][y] = 1


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(Q) != 0:
        t_xy = Q.pop(0)
        tx = t_xy[0]
        ty = t_xy[1]
        for z in range(4):
            testx = tx + dx[z]
            testy = ty + dy[z]
            if -1 < testx < N and -1 < testy < N:
                if data[testx][testy] == 0 and visited[testx][testy] == 0:
                    Q.append([testx, testy])
                    visited[testx][testy] = visited[tx][ty] + 1

                elif data[testx][testy] == 3 and visited[testx][testy] == 0:
                    visited[testx][testy] = visited[tx][ty] + 1
                    return


for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                rx = i
                ry = j
                bfs(i, j)

    result = 0

    for a in range(N):
        for b in range(N):
            if data[a][b] == 3 and visited[a][b] != 0:
                result = visited[a][b] - visited[rx][ry] - 1
            elif data[a][b] == 3 and visited[a][b] == 0:
                result = 0

    print('#{} {}'.format(tc, result))