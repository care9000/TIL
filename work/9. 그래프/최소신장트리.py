import sys
sys.stdin = open('최소신장트리_input.txt')

def MST():
    total = 0
    u = 0
    key[u] = 0

    for i in range(V+1): # 가중치 업데이트
        min = 998875462
        for v in range(V+1):
            if visit[v] == 0 and min > key[v]:
                min = key[v]
                u = v
        visit[u] = 1 # 방문처리
        total += connection[PI[u]][u]

        for v in range(V+1): # 인접 정점 가중치 업데이트
            if connection[u][v] != 0 and visit[v] == 0 and connection[u][v] < key[v]:
                key[v] = connection[u][v]
                PI[v] = u
    return total


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 마지막 노드번호(V), 간선의 개수(E)
    data = [list(map(int, input().split())) for _ in range(E)]
    # n1, n2, w(가중치)
    print(data)


    connection = [[0] * (V+1) for _ in range(V+1)]

    key = [97987987] * (V+1) #가중치
    visit = [0] * (V+1)
    PI = list(range(V+1))

    for i in range(len(data)):
        n1 = data[i][0]
        n2 = data[i][1]
        w = data[i][2]
        connection[n1][n2], connection[n2][n1] = w, w

    print('#{} {}'.format(tc, MST()))