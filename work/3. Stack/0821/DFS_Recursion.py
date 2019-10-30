import sys
sys.stdin = open('연습3_input.txt')

V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for i in range(V+1)]


for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1


# for i in range(V+1):
#     print('{} {}'.format(i, G[i]))

def dfs(v):
    visited[v] = 1
    print(v, end='-')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

    # for w in range(1, V+1):
    #     for j in range(1, V+1):
    #         if G[w][j] == 1 or G[j][w] == 1:
    #             if visited[j] == 0:
    #                 dfs(j)

dfs(1)
