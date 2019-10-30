import sys
sys.stdin = open('정곤_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    max_num = 0
    result = 0

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            test = data[i] * data[j]
            temp = []
            test_num = 0
            if test < 10:
                if test > max_num:
                    max_num = test

            elif test < max_num:
                continue

            else:
                while test != 0:
                    a = test % 10
                    if len(temp) == 0:
                        temp.append(a)
                        test = test // 10

                    elif len(temp) != 0:
                        if temp[-1] >= a:
                            temp.append(a)
                            test = test // 10

                            if test < 10: # 한자리 남았을때..
                                if temp[-1] >= test:
                                    temp.append(test)
                                    test -= test

                                n = 0
                                while test == 0 and len(temp) != 0:
                                    A = temp.pop(0)
                                    num = A * (10 ** n)
                                    test_num += num
                                    n += 1
                                if test_num > max_num:
                                    max_num = test_num
                        else:
                            result = -1
                            test -= test

    if max_num == 0:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, max_num))