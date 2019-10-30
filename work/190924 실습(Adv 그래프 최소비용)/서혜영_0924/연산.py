import sys
sys.stdin = open('연산_input.txt')

def calc(n):
    Q = []
    Q.append(n)
    visited[n] = 0

    i = 0
    while Q:
        a = Q[i]
        if a == M:
            break
        if 0 < a + 1 < 1000001 and visited[a + 1] == 0:
            Q.append(a+1)
            visited[a+1] = visited[a] + 1

        if 0 < a - 1 < 1000001 and visited[a - 1] == 0:
            Q.append(a - 1)
            visited[a - 1] = visited[a] + 1

        if 0 < a * 2 < 1000001 and visited[a * 2] == 0:
            Q.append(a * 2)
            visited[a * 2] = visited[a] + 1

        if 0 < a - 10 < 1000001 and visited[a - 10] == 0:
            Q.append(a - 10)
            visited[a - 10] = visited[a] + 1

        i += 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    calc(N)

    print('#{} {}'.format(tc, visited[M]))