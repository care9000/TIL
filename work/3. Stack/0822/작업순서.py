def dfs(v):
    if v in real_start:
        visited[v] = 1
        print(v, end=' ')

    if v not in real_start:
        for j in range(1, (len(temp) // 2) + 2, 2):
            if temp[j] == v:
                if visited[temp[j-1]] == 1:
                    visited[v] = 1
                    print(v, end=' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open('작업_input.txt')


T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(0, (len(temp)//2)+1, 2):
        G[temp[i]][temp[i + 1]] = 1

    start = {}

    for j in range(1, (len(temp)//2)+2, 2):
        if temp[j] not in start:
            start[temp[j]] = 1
        elif temp[j] in start:
            start[temp[j]] += 1
    # print(start)
    visited = [0] * (V+1)

    real_start = []
    for a in range(1, V + 1):
        real_start.append(a)

    for k in start.keys():
        real_start.remove(k)

    print('#{}'.format(tc), end=" ")

    for r in real_start:
        dfs(r)

    print()