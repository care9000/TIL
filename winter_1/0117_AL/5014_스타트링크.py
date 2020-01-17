import sys
sys.stdin = open('5014_스타트링크.txt')

import collections

def bfs(now):
    q = collections.deque([])
    q.append(now)

    while len(q):
        now = q.popleft()
        if now == G:
            return
        up = now + U
        down = now - D
        if up <= F and visited[up] == 0:
            visited[up] = visited[now] + 1
            q.append(up)
        if down > 0 and visited[down] == 0:
            visited[down] = visited[now] + 1
            q.append(down)



F, S, G, U, D = map(int, input().split())



visited = [0 for _ in range(F + 1)]
visited[0] = 1
visited[S] = 1


bfs(S)
if visited[G] - 1 == -1:
    print('use the stairs')
else:
    print(visited[G] - 1)