import sys
sys.stdin = open('전기_input.txt')

def charge(bat, start_point, cnt):
    # print(min_cnt)
    global min_cnt

    if cnt >= min_cnt:
        return

    else:
        for i in range(1, bat+1):
            # start_point += i
            if start_point + i <= N:
                if start_point + i == N:
                    if cnt < min_cnt:
                        min_cnt = cnt
                        return

                else:
                    charge(data[start_point + i], start_point + i, cnt+1)
            # else:
            #     cnt += 1


T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data.pop(0)
    data = [0] + data
    min_cnt = 99999

    # print(data)
    # print(N)
    # print(bus_stop)

    charge(data[1], 1, 0)

    print('#{} {}'.format(tc, min_cnt))