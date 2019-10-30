import sys
sys.stdin = open('최소비용_input.txt')

def road(x, y, fuel):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [[0, 0]]

    visited[0][0] = 0
    while stack:
        x, y = stack.pop(0)
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if -1 < nx < N and -1 < ny < N:

                if visited[nx][ny] > visited[x][y]:
                    alpha_fuel = data[nx][ny] - data[x][y]
                    if alpha_fuel < 0:
                        alpha_fuel = 0
                    if visited[nx][ny] > visited[x][y] + 1 + alpha_fuel:
                        visited[nx][ny] = visited[x][y] + 1 + alpha_fuel
                        stack.append([nx, ny])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [[99999] * N for _ in range(N)]
    # [print(data[i]) for i in range(len(data))]


    road(0, 0, 0)

    # print(visited)

    print('#{} {}'.format(tc, visited[N-1][N-1]))
    # [print(visited[i]) for i in range(len(visited))]
