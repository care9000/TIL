import sys
sys.stdin = open('상원이_input.txt')

def bfs(v):
    Q = []
    Q.append(v)
    friends[v] = 1


    while len(Q) != 0:
        t = Q.pop(0)
        for j in range(1, N+1):
            if visited[t][j] == 1 and friends[j] == 0:
                Q.append(j)
                friends[j] = friends[t] + 1
                # print(j, end='-')
                # print(visited)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    friends = [0] * (N+1)
    visited = [[0] * (N+1) for _ in range(N+1)]
    data = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(data)):
        a = data[i][0]
        b = data[i][1]
        visited[a][b], visited[b][a] = 1, 1

    bfs(1)

    cnt = 0
    for k in range(N+1):
        if friends[k] == 2 or friends[k] == 3:
            cnt += 1

    print('#{} {}'.format(tc, cnt))