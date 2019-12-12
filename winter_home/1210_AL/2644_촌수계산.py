import sys
sys.stdin = open('2644_촌수계산.txt')

import collections

def bfs(i):
    q = collections.deque([])
    q.append(i)

    while len(q):
        degree = q.popleft()
        for j in range(n):
            if graph[degree][j] and kinship[j] == 0:
                kinship[j] = kinship[degree] + 1
                if j == end:
                    return
                q.append(j)


# n = 사람의 수
n = int(input())

# start, end  계산해야할 촌 수
start, end = map(int, input().split())

# m = 촌수 계산해야할 부모-자식 의 번호
m = int(input())
node_list = [list(map(int, input().split())) for _ in range(m)]
graph = [[0] * n for _ in range(n)]

for node in node_list:
    graph[node[0] - 1][node[1] - 1] = 1
    graph[node[1] - 1][node[0] - 1] = 1

kinship = [0] * n
kinship[start - 1] = 1
bfs(start - 1)
# print(kinship)
print(kinship[end - 1] - 1)