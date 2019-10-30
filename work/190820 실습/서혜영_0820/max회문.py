import sys
sys.stdin = open('회문2_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    arr = [list(input()) for _ in range(100)]
    result = 0

    for l in range(100, 0, -1):
        for k in range(100):
            cnt = 0
            for j in range(100-l+1):
                for i in range(l//2):
                    if arr[k][i+j] == arr[k][j+l-1-i]:
                        cnt += 1
                        if cnt == (l//2):
                            result = (99-i) - i + 1
                            break
                    else:
                        break
        if result == 0:
            for l in range(100, -1, -1):
                for k in range(100):
                    cnt = 0
                    for i in range(l//2):
                        if arr[i][k] == arr[99-i][k]:
                            cnt += 1
                            if cnt == (l//2):
                                result = (100-i) - i + 1
                                break
                        else:
                            break

    print('#{} {}'.format(tc, result))