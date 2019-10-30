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
    cnt = 0
    cnt2 = 0
    for l in range(100, -1, -1): # 길이 1~100
        for h in range(100):
            for i in range(100-l+1): # 길이에 따른 반복 횟수
                result = []
                result2 = []
                for j in range(l): # 길이만큼 추가하기
                    result.append(arr[h][i+j])
                    result2.append(arr[i+j][h])
                if result == result[::-1]:
                    cnt += 1
                if result2 == result2[::-1]:
                    cnt2 += 1

                if cnt == 1 or cnt2 == 1 :
                    max_len = l
                if max_len > max_len1:
                    max_len1 = max_len


    print('#{} {}'.format(tc, max_len1))