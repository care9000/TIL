import sys
sys.stdin = open('피자_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_idx = pizza[::1]
    stove = []
    idx = []


    while len(pizza) > 0:
        sample = pizza.pop(0)
        stove.append(sample)
        idx.append(pizza_idx.index(sample)+1)

        if len(stove) == N and len(pizza) != 0: # 피자 굽기
            while stove[0] != 0:
                if stove[0] != 0:
                    half_pizza = stove.pop(0)
                    a = half_pizza//2
                    if a != 0:
                        stove.append(a)
                        h_p_idx = idx.pop(0)
                        idx.append(h_p_idx)
                    else:
                        idx.pop(0)
                        if len(pizza) != 0:
                            idx.append(pizza_idx.index(pizza[0]) + 1)
                            stove.append(pizza.pop(0))


            if stove[0] == 0:
                stove.pop(0)
                idx.pop(0)
        elif len(stove) <= N and len(pizza) == 0:
            while stove[0] != 0:
                half_pizza = stove.pop(0)
                a = half_pizza // 2
                if a != 0:
                    stove.append(a)
                    h_p_idx = idx.pop(0)
                    idx.append(h_p_idx)

            if stove[0] == 0:
                stove.pop(0)
                result = idx.pop(0)

    print(result)
    # if len(pizza) == 0:
    #     if len(stove) > 1:





    # for i in range(1, N + 1):
    #     empty_stove = N
    #     if stove[i] == 0:
    #         empty_stove += 1
    #
    # if empty_stove == N - 1: