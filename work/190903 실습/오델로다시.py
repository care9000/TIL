import sys
sys.stdin = open('오셀로_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    for _ in range(M):
        data.append(list(map(int, input().split())))
    table = [[0] * (N+1) for _ in range(N+1)]
    C = N // 2
    # 2 백돌 놓기
    table[C][C] = 2
    table[C+1][C+1] = 2
    # 1 흑돌 놓기
    table[C][C+1] = 1
    table[C+1][C] =1
    # print(table)
    # print(data)

    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]

    for i in range(M):
        color = data[i][2]
        x = data[i][0]
        y = data[i][1]
        table[y][x] = color
