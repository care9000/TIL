def dfs(i, j):

    visited[i][j] = 1

    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    # if 1 <= i <= 98 and 1 <= j <= 98:
    #     if arr[i][j-1] == 1 and visited[i][j-1] == 0:
    #         dfs([i][j-1])
    #     elif arr[i][j+1] == 1 and visited[i][j+1] == 0:
    #         dfs([i][j+1])
    #     else:
    #         dfs([i-1][j])

    for z in range(3):
        testX = i + dx[z]
        testY = j + dy[z]
        if -1 < testX < 100 and -1 < testY < 100:
            if arr[i][testY] == 1 and visited[i][testY] == 0:
                dfs(i, testY)
            if arr[testX][j] == 1 and visited[testX][j] == 0:
                dfs(testX, j)



import sys
sys.stdin = open('사다리_input.txt')

T = 10

arr = [[0 for _ in range(100)] for _ in range(100)]
visited = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(1, 11):
    N = int(input())
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    # print(arr)

    for j in range(99, -1, -1): # 출발지 찾기
        for k in range(99, -1, -1):
            if arr[j][k] == 2:
                # print(j, k)
                dfs(j, k)

        for a in range(100):
            if visited[0][a] == 1:
                result = a
    # print(visited)
    print('#{} {}'.format(tc, result))





