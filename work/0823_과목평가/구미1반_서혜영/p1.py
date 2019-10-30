import sys
sys.stdin = open('색칠_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a = list(map(int, input().split()))
        data.append(a)

    for k in range(M):
        x = data[k][2] - data[k][0]
        y = data[k][3] - data[k][1]
        for i in range(data[k][0], data[k][0]+x+1):
            for j in range(data[k][1], data[k][1]+y+1):
                arr[i][j] = 1
    cnt = 0
    for c in range(N):
        for d in range(N):
            if arr[c][d] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
