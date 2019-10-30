import sys
sys.stdin = open('상원이_input.txt')


def dfs(n):
    friends[n] = 1

    cnt1 = 0
    for k in range(len(data)):
        if data[k][0] == 1:
            cnt1 += 1

    if cnt1 == 0:
        return


    for i in range(len(data)):
        if visited[n][i] == 1 and friends[i] == 0:
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    friends = [0] * (N+1)
    visited = [[0] * (N+1) for _ in range(N+1)]
    data = [list(map(int, input().split())) for _ in range(M)]

    for a in range(len(data)):
        x = data[a][0]
        y = data[a][1]
        visited[x][y] = 1

    dfs(1)

    result = 0
    if friends[1] == 1:
        for j in range(len(friends)):
            if friends[j] == 1:
                result += 1


    print(friends)
    print(result)
    print('#{} {}'.format(tc, result-1))