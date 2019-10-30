import sys
sys.stdin = open('2048_input.txt')

T = int(input())

for tc in range(1, T+1):
    n, D = input().split()
    N = int(n)
    data = [list(map(int, input().split())) for _ in range(N)]
    dd = [0, 0]

    if D == 'up':
        dd = [-1, 0]
    elif D == 'dowm':
        dd = [1, 0]
    elif D == 'right':
        dd = [0, 1]
    else: #왼쪽
        dd = [0, -1]
    print(tc)
    [print(data[i]) for i in range(len(data))]
    result = []
    # 좌우
    if D == 'right' or D == 'left':
        for i in range(N):
            calc = []
            temp = []
            cnt0 = 0
            for j in range(N):
                if data[i][j] == 0:
                    cnt0 += 1
                    if j == N-1 and len(calc) != 0:
                        temp.append(calc.pop())

                elif len(calc) == 0:
                    calc.append(data[i][j])

                elif 1 <= j < N and len(calc) == 1:
                    if calc[-1] != data[i][j]:
                        temp.append(calc.pop())
                        calc.append(data[i][j])
                        if j == N-1:
                            temp.append(calc.pop())

                    elif calc[-1] == data[i][j]:
                        calc.pop()
                        temp.append(data[i][j] * 2)


            print(cnt0)
            result.append(temp)
    print(result)






    # 상하
    # if D == 'up' or D == 'down':



