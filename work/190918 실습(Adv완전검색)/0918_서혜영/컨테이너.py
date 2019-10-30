import sys
sys.stdin = open('컨테이너_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테N, 트럭M
    weight = list(map(int, input().split())) # 컨테이너 무게
    trucks = list(map(int, input().split()))
    #
    # print(N, M)
    # print(weight)
    # print(trucks)

    weight = sorted(weight)
    trucks = sorted(trucks)

    # print(weight)
    # print(trucks)


    cnt = 0


    for _ in range(len(trucks)):
        if len(trucks) != 0 and len(weight) != 0:

            if trucks[-1] < weight[-1]:
                weight.pop()
            elif trucks[-1] >= weight[-1]:
                selec_t = trucks.pop()
                cnt += weight[-1]
                weight.pop()

    print('#{} {}'.format(tc, cnt))