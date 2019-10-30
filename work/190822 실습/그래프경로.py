def dfs(v):
    if visited[v] == 1:
        return
    else:
        visited[v] = 1
        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:
                dfs(w)

import sys
sys.stdin = open('그래프_input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    datas = []
    result = 0
    for _ in range(E+1):
        a = list(map(int, input().split()))
        datas.append(a)
    a = datas[-1] # S, G
    S = a[0]
    G = a[1]
    datas.pop()

    for x in range(len(datas)):
        i = datas[x][0]
        j = datas[x][1]
        arr[i][j] = 1 # 인접행렬 체크

    dfs(S)

    if visited[S] == 1 and visited[G] == 1:
        result += 1

    print('#{} {}'.format(tc, result))