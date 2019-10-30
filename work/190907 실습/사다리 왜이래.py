import sys
sys.stdin = open('ladder2_input.txt')

def bfs(x, y):
    Q = []
    Q.append([x, y])
    visited[x][y] = 1

    dx = [0, 0, 1]
    dy = [1, -1, 0]

    while len(Q) != 0:
        testxy = Q.pop(0)
        for z in range(3):
            nx = testxy[0] + dx[z]
            ny = testxy[1] + dy[z]

            if -1 < nx < 100 and -1 < ny < 100:

                if nx == 99:
                    if sum(visited[99]) != 0:
                        return

                if visited[nx][ny] == 0 and ladder[nx][ny] == 1:
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[testxy[0]][testxy[1]] + 1

T = 10

for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 출발지 찾기

    result = []
    for i in range(13):
        visited = [[0] * 100 for _ in range(100)]
        if ladder[0][i] == 1:

            bfs(0, i)

            print(visited)
        for j in range(100):
            if visited[99][j] != 0:
                result.append([visited[99][j], j])
    print(result)