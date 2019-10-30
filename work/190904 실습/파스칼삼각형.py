import sys
sys.stdin = open('파스칼_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    triangle = []
    for i in range(N):
        triangle.append([0]*(i+1))

    for j in range(N):
        triangle[j][0] = 1
        triangle[j][-1] = 1


    for k in range(2, N):
        for l in range(1, k):
            triangle[k][l] = triangle[k-1][l-1] + triangle[k-1][l]

    print('#{}'.format(tc))
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=' ')
        print()


    # for i in range(N):
    #     temp = []
    #     for j in range(N):
    #         if i < 2 and j < 2 and len(triangle) < 2:
    #             triangle.append([1]*(i+j+1))
    #
    #
    #
    #         elif len(triangle) >= 2:
    #
    #             if j == 0:
    #                 temp.append(1)
    #
    #             elif 1 <= j < N-1:
    #                 num = triangle[i][j-1] + triangle[i][j]
    #                 temp.append(num)
    #
    #                 if j == N-2:
    #                     temp.append(1)
    #                     triangle.append(temp)
    #
    #                     if len(triangle) == N:
    #                         break
