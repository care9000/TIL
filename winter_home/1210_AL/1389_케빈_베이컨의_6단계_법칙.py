import sys
sys.stdin = open('1389_케빈_베이컨의_6단계_법칙.txt')

import collections

def bfs(start):
    q = collections.deque([])
    q.append(start)
    while len(q):
        tem_start = q.popleft()
        for j in range(N):
            if graph[tem_start][j] and visited[j] == 0:
                visited[j] = visited[tem_start] + 1
                q.append(j)
N, M = map(int, input().split())
node_list = [list(map(int, input().split())) for _ in range(M)]

graph = [[0] * N for _ in range(N)]

for node in node_list:
    graph[node[0] - 1][node[1] - 1] = 1
    graph[node[1] - 1][node[0] - 1] = 1

cnt = 0
min =987654321
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    bfs(i)
    if sum(visited) < min:
        min = sum(visited)
        cnt = i + 1
print(cnt)

