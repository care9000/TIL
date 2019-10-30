import sys
sys.stdin = open("파리_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M =  map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cur_sum = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    cur_sum += arr[a][b]
            if max_sum < cur_sum:
                max_sum = cur_sum

    print('#{} {}'.format(tc, max_sum))
