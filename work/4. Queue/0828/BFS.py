def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    print(v, end='-')

    while len(Q) != 0:
        t = Q.pop(0)
        for j in range(1, V+1):
            if arr[t][j] != 0 and visited[j] == 0:
                Q.append(j)
                visited[j] = visited[t] + 1
                print(j, end='-')
                print(visited)

V, E = 7, 8
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]


visited = [0] * (V+1)
arr = [[0] * (V+1) for _ in range(V+1)]

for i in range(0, len(data), 2):
    x = data[i]
    y = data[i+1]
    arr[x][y] = 1
    arr[y][x] = 1

for k in range(V+1):
    print('{} {}'.format(k, arr[k]))



bfs(1)