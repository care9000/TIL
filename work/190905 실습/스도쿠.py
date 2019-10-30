import sys
sys.stdin = open('스도쿠_input.txt')

T = int(input())

for tc in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]

    # print(sdoku)

    # 가로
    total = 0
    for i in range(9):
        cnt1 = 0
        check = [0] * 10
        for j in range(9):
            check[sdoku[i][j]] = 1
        for k in range(1, 10):
            if check[k] == 1:
                cnt1 += 1
        if cnt1 == 9:
            total += 1
    # 세로

    for i in range(9):
        cnt2 = 0
        check = [0] * 10
        for j in range(9):
            check[sdoku[j][i]] = 1
        for k in range(1, 10):
            if check[k] == 1:
                cnt2 += 1
        if cnt2 == 9:
            total += 1
    # 네모

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt3 = 0
            check = [0] * 10
            for k in range(3):
                for l in range(3):
                    check[sdoku[i+k][j+l]] = 1

                for k in range(1, 10):
                    if check[k] == 1:
                        cnt3 += 1
                if cnt3 == 9:
                    total += 1

    result = 0
    if total == 27:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))

