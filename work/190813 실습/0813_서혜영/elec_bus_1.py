import sys
sys.stdin = open('input_elec.txt')

T = int(input())

for tc in range(T):
    K, N, M = list(map(int, input().split()))
    # print(K, N, M)
    data = list(map(int, input().split()))
    # print(data)
    gps = 0
    cnt = 0

    for i in range(M):
        # print(i)
        if i < (M-1):
            if data[i] - gps < K and data[i+1] - gps >= K:
                cnt += 1
                gps = data[i+1]
            if data[i] - gps < K and data[i+1] - gps < K:
                gps = data[i+1]
        # # if i < (M-1) and data[i] - gps > K or data[i+1] - gps > K:
        # #     break
        #     # print(cnt)
        #     # print(gps)
        # if i == (M-1) and N - gps > K:
        #     cnt += 1
        #     gps = data[i]
        # if i == (M-1) and N - gps <= K:
        #     cnt += 0
        #     gps = data[i]
        #     # print(cnt)
        #     # print(gps)\
    print(cnt)
    print(gps)

