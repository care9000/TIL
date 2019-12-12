import sys
sys.stdin = open('DFS와 BFS.txt')

def dfs(i):
    global cnt_dfs
    result_dfs.append(i)
    cnt_dfs += 1
    visited_dfs[i] = cnt_dfs
    for j in range(len(data[i])):
        if data[i][j] == 1 and visited_dfs[j] == 0:
            dfs(j)

def bfs(i):
    global cnt_bfs
    result_bfs.append(i)
    cnt_bfs += 1
    visited_bfs[i] = cnt_bfs
    k = 0
    q = []
    cnt = visited_bfs[i]
    q.append(i)
    while len(q) != 0 :
        a = q.pop(0)
        for l in range(len(data[a])):
            if data[a][l] == 1 and visited_bfs[l] == 0:
                cnt +=1
                visited_bfs[l] = cnt
                result_bfs.append(l)
                q.append(l)





N, M, V = map(int, input().split())
visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]
result_dfs = []
result_bfs = []
dummy = [list(map(int, input().split())) for _ in range(M)]
data = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(len(dummy)):
    data[dummy[i][0]][dummy[i][1]] = 1
    data[dummy[i][1]][dummy[i][0]] = 1

visited_dfs[V] = 1
cnt_dfs = visited_dfs[V]
result_dfs.append(V)
for i in range(len(data[V])):
    if data[V][i] == 1 and visited_dfs[i] == 0:
        dfs(i)
visited_bfs[V] = 1
cnt_bfs = visited_bfs[V]
bfs(V)

for i in result_dfs:
    print(i, end = " ")
print()
for i in result_bfs:
    print(i, end = " ")
