import sys
sys.stdin = open('input_elec.txt')

T = int(input())

for tc in range(T):
    K, N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    gps = 0
    cnt = 0

    # for i in range(M):
    #     if data[i] != gps:
    #         if i < (M-1):
    #             if data[i] - gps <= K and data[i+1] - gps >= K:
    #                 cnt += 1
    #                 gps = data[i+1]
    #             elif data[i] - gps < K and data[i+1] - gps < K:
    #                 gps = data[i+1]
    #             elif data[i] - gps > K or data[i+1] - data[i] > K:
    #                 cnt = 0
    #                 break
    #         elif i == (M-1):
    #             if N - data[i] <= K:
    #                 cnt += 1
    #                 gps = data[i]
    #             else:
    #                 cnt = 0
    #                 break
    #
    # print('#{} {} '.format(tc+1 , cnt))
    # print(cnt)
    # print(gps)

    for i in range(M):
        if i < M-1:
            if data[i] - gps < M:
                if data[i+1] - gps > M:
                    cnt += 1
                    gps = data[i]
                else:
                    gps = data[i]
            elif data[i] - gps >= M:
                cnt += 1
                gps = data[i]

        if i >= M:
            if data[i] - gps >= M:
                cnt += 1
                gps = data[i]
            if N - data[i] >= M:
                cnt += 1
                gps = data[i]

    print('#{} {} '.format(tc + 1, cnt))
