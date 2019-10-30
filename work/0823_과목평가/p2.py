import sys
sys.stdin = open('사각테두리_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_value = 0

    for i in range(M-K+1):
        for j in range(N-K+1):
          value = 0
          # 일단 더하고..
          for a in range(i, i+K):
              for b in range(j, j+K):
                  value += arr[b][a]

            # 가운데 빼자....
          for x in range(1, (K//2)+1):
              for y in range(1, (K//2)+1):
                  value -= arr[j+y][i+x]

          if value > max_value:
            max_value = value

    print('#{} {}'.format(tc, max_value))