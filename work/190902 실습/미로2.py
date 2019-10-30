import sys
sys.stdin = open('미로2_input.txt')


def bfs(x, y): #
    Q = []
    Q.append([x, y])
    visited[x][y] = 9 # 방문표시

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(Q) != 0:
        txy = Q.pop(0)
        tx = txy[0]
        ty = txy[1]
        for z in range(4):
            testx = tx + dx[z]
            testy = ty + dy[z]
            if -1 < testx < 100 and -1 < testy < 100:
                if arr[testx][testy] == 0 and visited[testx][testy] == 0:
                    Q.append([testx, testy])
                    visited[testx][testy] = 9
                elif arr[testx][testy] == 3 and visited[testx][testy] == 0:
                    visited[testx][testy] = 9
                    return


T = 10

for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * 100 for _ in range(100)]
    arr = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2: # 2 출발지
                bfs(i, j)

    flag = 0
    for a in range(100):
        for b in range(100):
            if arr[a][b] == 3 and visited[a][b] == 9: # 3 도착지
                flag = 1

    print('#{} {}'.format(tc, flag))
