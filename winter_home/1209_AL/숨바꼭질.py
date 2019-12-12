import sys
sys.stdin = open('숨바꼭질.txt')

import collections

def bfs(start, sec):
    global K, cnt
    q = collections.deque([])
    q.append([start, sec])
    while len(q):
        now_subin, now_sec = q.popleft()
        if now_subin - 1 == K or now_subin + 1 == K or now_subin * 2 == K:
            cnt = now_sec + 1
            return
        if now_subin - 1 > -1 and visited[now_subin - 1] == 0:
            visited[now_subin - 1] = 1
            q.append([now_subin - 1, now_sec + 1])
        if now_subin + 1 < 100003 and visited[now_subin + 1] == 0:
            visited[now_subin + 1] = 1
            q.append([now_subin + 1, now_sec + 1])
        if now_subin * 2 < 100003 and visited[now_subin * 2] == 0:
            visited[now_subin * 2] = 1
            q.append([now_subin * 2, now_sec + 1])




N, K = map(int, input().split())
visited = [0] * 100003
cnt = 0
visited[N] = 1
if N == K:
    cnt = 0

else:
    bfs(N, 0)
print(cnt)