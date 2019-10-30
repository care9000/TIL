import sys
sys.stdin = open('색칠하기_input.txt')

T = int(input())
for tc in range(T):
    data = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    for _ in range(N):
        a, b, c, d, e = map(int, input().split())

        # print(N)
        # print(a, b, c, d, e)
        if e == 1:
            for i in range(a, c+1):
                for j in range(b, d+1):
                    data[i][j] += e

        elif e == 2:
            for i in range(a, c+1):
                for j in range(b, d+1):
                    data[i][j] += e
    cnt = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))