import sys
sys.stdin = open('부분집합_input.txt')

T = int(input())
for tc in range(T):
    N, K = list(map(int, input().split()))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    cnt = 0

    for i in range(1<<n):
        result = []

        for j in range(n+1):
            if i & (1<<j):
                result.append(arr[j])
        #         print(arr[j], end=', ')
        # print()

        if len(result) == N and sum(result) == K: 
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))
