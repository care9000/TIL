import sys
sys.stdin = open('회문_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    #N*N 정렬, M 길이 회문
    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    for i in range(N):
        for j in range(N-M+1):
            test = []
            for k in range(j, j+M):
                test.append(arr[i][k])
            if test == test[::-1] and len(test) == M:
                result = test


    for i in range(N):
        for j in range(N-M+1):
            test = []
            for k in range(j, j+M):
                test.append(arr[k][i])
            if test == test[::-1] and len(test) == M:
                result = test


    bingo = ''.join(result)
    print('#{} {}'.format(tc, bingo))
    print('# %d %d' % (tc, bingo))