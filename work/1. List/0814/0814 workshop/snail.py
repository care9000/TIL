import sys
sys.stdin = open('snail_input.txt')\

def isFill(N, x, y):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    return False

T = int(input())
for tc in range(T):
    N = int(input())
    row, col = N, N
    data = [[0 for _ in range(col)] for _ in range(row)]

    # print(data)
    for i in range(N):
        for j in range(N):
            if isFill(N, i, j) == False:
                data[i][j] = (j+1)
            if isFill(N, i, j):

    print(data)