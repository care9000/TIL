import sys
sys.stdin = open('최소이동거리_input.txt')

def min_dis(x):
    Q = []
    key[x] = 0
    Q.append(x)

    while Q:
        a = Q.pop(0)
        for i in range(len(data)):
            if data[i][0] == a:
                if key[a] + data[i][2] < key[data[i][1]]:
                    key[data[i][1]] = key[a] + data[i][2]
                    Q.append(data[i][1])


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split()) # 도착지 N
    data = [list(map(int, input().split())) for _ in range(E)]


    key = [97987987] * (N+1) #가중치

    min_dis(0)

    print('#{} {}'.format(tc, key[-1]))