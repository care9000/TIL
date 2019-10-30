import sys
sys.stdin = open('배열회전_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result1 = []
    result2 = []
    result3 = []
    # print(arr)
    # for k in range(3): # 3번 뒤집을
    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(arr[j][i])
        result1.append(temp)


    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(result1[j][i])
        result2.append(temp)

    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(result2[j][i])
        result3.append(temp)
    print('#{}'.format(tc))

    # 출력
    for i in range(N):
        for j in range(N):
            print(result1[i][j],end="")
        print(end=" ")

        for j in range(N):
            print(result2[i][j],end="")
        print(end=" ")

        for j in range(N):
            print(result3[i][j],end="")
        print()