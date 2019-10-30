def dfs(i, j):
    if cnt == 0:
        visited[i][j] = 1
    elif cnt == 1:
        visited[i][j] = 2
    elif cnt == 2:
        visited[i][j] = 3


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for z in range(4):
        testX = i + dx[z]
        testY = j + dy[z]
        if -1 < testX < 7 and -1 < testY < 7:
            if arr[testX][testY] == 1 and visited[testX][testY] == 0:
                dfs(testX, testY)

import sys
sys.stdin = open('두더지_input.txt')
N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

cnt = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1 and visited[x][y] == 0:
            dfs(x, y)
            cnt += 1

# for i in range(N):
#     print('{} {}'.format(i, visited[i]))

cnt1 = 0
cnt2 = 0
cnt3 = 0

for x in range(N):
    for y in range(N):
        if visited[x][y] == 1:
            cnt1 += 1
        elif visited[x][y] == 2:
            cnt2 += 1
        elif visited[x][y] == 3:
            cnt3 += 1

print(cnt)
print(cnt3)
print(cnt2)
print(cnt1)

