import sys
sys.stdin = open('보급로_input.txt')


def bfs(x, y, t):
    Q = []
    Q.append([x, y])
    visited[x][y] = t

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while Q != 0:
        nxy = Q.pop(0)
        v_up = 0
        v_down = 0
        v_r = 0
        v_l = 0
        for z in range(4):
            nx = nxy[0] + dx[z]
            ny = nxy[1] + dy[z]
            if -1 < nx < N and -1 < ny < N:
                if j == 0: #왼
                    v_l += map[nx][ny]
                    if -1 < nx + dx[z] < N and -1 < ny + dy[z] < N:
                        v_l += map[nx + dx[z]][ny + dy[z]]

                elif j == 1: #오
                    v_r += map[nx][ny]
                    if -1 < nx + dx[z] < N and -1 < ny + dy[z] < N:
                        v_r += map[nx + dx[z]][ny + dy[z]]

                elif j == 2: #위
                    v_up += map[nx][ny]
                    if -1 < nx + dx[z] < N and -1 < ny + dy[z] < N:
                        v_up += map[nx + dx[z]][ny + dy[z]]

                elif j == 3: #아래
                    v_down += map[nx][ny]
                    if -1 < nx + dx[z] < N and -1 < ny + dy[z] < N:
                        v_down += map[nx + dx[z]][ny + dy[z]]

                v_min = [v_l, v_r, v_up, v_down]
                min_d = min(v_min)
                D = v_min.index(min_d)

        if visited[nxy[0] + dx[D]][nxy[1] + dy[D]] == 0:
            Q.append([nxy[0] + dx[D], nxy[1] + dx[D]])
            t += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    map = []
    for i in range(N):
        map.append(list(input()))

    for i in range(N):
        for j in range(N):
            map[i][j] = int(map[i][j])

    bfs(0, 0, 1) # 출발@
    print(map)
    print(visited)