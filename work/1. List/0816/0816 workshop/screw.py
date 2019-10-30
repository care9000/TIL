import sys
sys.stdin = open('screw_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    screw = list(map(int, input().split()))

    result = []
    cnt = 0
    for i in range(N):
        a = screw[:2]
        del screw[:2]

        if cnt == 0:
            result = result.append(a)
            cnt += 1


        elif cnt != 0:
            for k in range(N):
                for l in range(1, k+1):
                    if a[0] == result[l-1][1]:
                        result.insert(l, a)

                    elif a[1] == result[l-1][0]:
                        result.insert(l-1, a)
        cnt += 1
        # elif cnt != 0:
        #     if a[0] == result[i-1][1]:
        #         result[i] = a
        #
        #     elif a[1] == result[0][0]:
        #         result[0], result[1] = a, result[0]

        print(result)


