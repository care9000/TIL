import sys
sys.stdin = open('파리_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    print(N, M)
    print(data)

    # for i in range(M-N+1):
    #     for j in range(M-N+1):

