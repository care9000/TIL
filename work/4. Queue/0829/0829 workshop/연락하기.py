import sys
sys.stdin = open('연락_input.txt')

def bfs(v):
    Q = []

    Q.append(v)
    visited[v] = 1

    while len(Q) != 0:
        t = Q.pop(0)
        for j in range(1, 101):
            if arr[t][j] == 1 and visited[j] == 0:
                Q.append(j)
                visited[j] = visited[t] + 1

T = 10

for tc in range(1, T+1):
    L, S = map(int, input().split())
    arr = [[0] * 101 for _ in range(101)]
    visited = [0] * 101
    contact = list(map(int, input().split()))
    for i in range(0, L, 2):
        x = contact[i]
        y = contact[i+1]
        arr[x][y] = 1

    bfs(S)

    nums = []
    for k in range(1, len(visited)):
        if visited[k] != 0:
            nums.append(visited[k])

    max_num = 0
    for max in nums:
        if max > max_num:
            max_num = max

    result = 0
    for l in range(1, len(visited)):
        if visited[l] == max_num:
            result = l

    print('#{} {}'.format(tc, result))
