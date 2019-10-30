import sys
sys.stdin = open('그룹나누기_input.txt')

def dfs(x):

    if people[x] == 0:
        people[x] = cnt

    for i in range(1, N+1):
        if couple[x][i] == 1 and people[i] == 0:
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 1번부터 N번
    data = list(map(int, input().split()))
    couple = [[0] * (N+1) for _ in range(N+1)] # 짝지 표시
    people = [0] * (N+1) # 방문표시

    for i in range(0, len(data), 2):
        couple[data[i]][data[i+1]], couple[data[i+1]][data[i]] = 1, 1

    cnt = 0

    for i in range(1, N+1):
        if people[i] == 0:
            cnt += 1
            dfs(i)

    print('#{} {}'.format(tc, cnt))