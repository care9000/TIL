import sys
sys.stdin = open('2048_input.txt')

T = int(input())

for tc in range(1, T+1):
    n, D = input().split()
    N = int(n)
    data = [list(map(int, input().split())) for _ in range(N)]
    dd = [0, 0]

    if D == 'up':
        dd = [-1, 0]
    elif D == 'dowm':
        dd = [1, 0]
    elif D == 'right':
        dd = [0, 1]
    else: #왼쪽
        dd = [0, -1]

    if D == 'up' or D == 'left':
        for i in range(N):
            for j in range(N):
                x = i + dd[0]
                y = j + dd[1]
                if -1 < x < N and -1 < y < N:
                    if data[x][y] == 0:
                        data[i][j], data[x][y] = data[x][y], data[i][j]

    elif D == 'down' or D == 'right':
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                x = i + dd[0]
                y = j + dd[1]
                if -1 < x < N and -1 < y < N:
                    if data[x][y] == 0:
                        data[i][j], data[x][y] = data[x][y], data[i][j]

    print(tc)
    [print(data[i]) for i in range(len(data))]