import sys
sys.stdin = open('ladder2_input.txt')

def bfs(x, y):
    Q = []
    Q.append([x, y])
    visited[x][y] = 1

    dx = [1, 0, 0]
    dy = [0, -1, 1]

    while len(Q) != 0:
        testxy = Q.pop(0)
        for z in range(3):
            nx = testxy[0] + dx[z]
            ny = testxy[1] + dy[z]

            if -1 < nx < 9 and -1 < ny < 13:

                if nx == 7:
                    if sum(visited[7]) != 0:
                        return

                if visited[nx][ny] == 0 and ladder[nx][ny] == 1:
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[testxy[0]][testxy[1]] + 1

T = 1

for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(8)]

    # 출발지 찾기

    result = []
    for i in range(13):
        visited = [[0] * 13 for _ in range(8)]
        if ladder[0][i] == 1:

            bfs(0, i)

            print(visited)
        for j in range(13):
            if visited[7][j] != 0:
                result.append([visited[7][j], j])
    print(result)
    Result = sorted(result)
    # print(Result)
        # for k in range(len(Result)):
    if Result[0][0] == Result[1][0]:
        C = Result[0][0]
        k = 0
        min_y = 0
        while Result[k][0] == C:
            min_y = Result[k][1]
            k += 1
            if k == len(Result):
                break
    # #
    # #
    # # for l in range(8):
    # #     print(visited[l])
    #
    # print(result)
    print(min_y)
