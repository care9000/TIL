import sys
sys.stdin = open('보급로_input.txt')


def bfs(x, y, t):
    Q = []
    Q.append([x, y])
    visited[x][y] = t

    dx = [0, 1]
    dy = [1, 0]
    while Q != 0:
        nxy = Q.pop(0)
        compare = []
        for z in range(2):
            nx = nxy[0] + dx[z]
            ny = nxy[1] + dy[z]
            if -1 < nx < N and -1 < ny < N:
                compare.append(map[nx][ny])
                if compare[0] == compare[1]:

                    

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