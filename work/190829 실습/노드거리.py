import sys
sys.stdin = open('노드_input.txt')

T = int(input())

def bfs(v):
    Q.append(v)
    visited[v] = 1


    while len(Q) != 0:
        t = Q.pop(0)
        for j in range(1, V+1):
            if arr[t][j] == 1 and visited[j] == 0:
                Q.append(j)
                visited[j] = visited[t] + 1


for tc in range(1, T+1):
    V, E = map(int, input().split()) # V가 노드, E는 간선
    visited = [0] * (V+1)
    data = []
    arr = [[0] * (V+1) for _ in range(V+1)]
    Q = []
    for _ in range(E+1):
        D = list(map(int, input().split()))
        data.append(D)

    sg = data.pop() # 출발, 도착 정보
    S = sg[0]
    G = sg[-1]
    for i in range(E):
        a = data[i][0]
        b = data[i][1]
        arr[a][b] = 1
        arr[b][a] = 1

    bfs(S)
    result = visited[G] - visited[S]
    if result < 0:
        result = 0

    print('#{} {}'.format(tc, result))