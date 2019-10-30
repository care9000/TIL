import sys
sys.stdin = open('회문2_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    arr = [list(input()) for _ in range(100)]
    # print(N)
    # print(arr)
    max_len = 0
    max_len1 = 0
    max_len2 = 0

    for l in range(100, -1, -1): # 길이 1~100
        cnt = 0
        for k in range(100):
            result = []
            for i in range(100-l+1): # 길이에 따른 반복 횟수
                for j in range(l): # 길이만큼 추가하기
                    result.append(arr[k][i+j])
                if result == result[::-1]:
                    cnt += 1
                if cnt == 1:
                    max_len = len(result)
                    break

        if cnt == 0:
            for k in range(100):
                result = []
                for i in range(100-l+1):
                    for j in range(l):
                        result.append(arr[i+j][k])
                    if result == result[::-1]:
                        cnt += 1
                    if cnt == 1:
                        max_len = len(result)


        # if max_len1 > max_len2:
        #     max_len = max_len1
        # else:
        #     max_len = max_len2

    print('#{} {}'.format(tc, max_len))