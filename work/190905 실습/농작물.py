import sys
sys.stdin = open('농작물_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]


    result = 0
    if N == 1:
        result = farm[0][0]

    else:
        c = N // 2
        for i in range(N): #가운데
            result += farm[i][c]

        l_col = 1
        while l_col <= c:
            for a in range(c): # 0, 1
                # 좌 0 ~ c-1
                for l in range(l_col, N - l_col):
                    result += farm[l][c-a-1]
                l_col += 1

        r_col = 1
        while r_col <= c:
            for b in range(c):
                # 우 c+1 ~ N-1
                for r in range(r_col, N - r_col):
                    result += farm[r][c+b+1]
                r_col += 1

    print('#{} {}'.format(tc, result))