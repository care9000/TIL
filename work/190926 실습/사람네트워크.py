import sys
sys.stdin = open('사람_input.txt')

def AllPairsShortest():
    for k in range(N):
        for i in range(N):
            if i != k :
                for j in range(N):
                    if j != k and j != i:
                        network[i][j] = min(network[i][k] + network[k][j], network[i][j])

T = int(input())

for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp.pop(0)

    network = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            network[i].append(temp[N*i + j])

    for i in range(N):
        for j in range(N):
            if i != j and network[i][j] == 0:
                network[i][j] = 999999

    # for i in range(len(network)):
    #     print(network[i])

    AllPairsShortest()

    min_value = 999999

    for i in range(len(network)):
        a = sum(network[i])
        if a < min_value:
            min_value = a

    print('#{} {}'.format(tc, min_value))
