import sys
sys.stdin = open('연산_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))

    print(data)

    num1 = max(data)
    num2 = min(data)

    arr = [0]
    a = 1
    cnt1 = 1
    while arr[-1] <= num1:
        arr.append(a)
        cnt1 += 1
        a = a + cnt1

    l_num = arr[-1]
    l_idx = arr.index(l_num)
    l = 1

    while l_num != num1:
        l_num -= 1
        l_idx -= 1
        l += 1

    l_idx_set = [l_idx, l] # 큰수 조ㅏ표


    s_num = 0
    s_idx = 0
    s = 1
    for i in range(len(arr)):
        if arr[i] >= num2:
            s_num = arr[i]
            s_idx = arr.index(s_num)
            break

    while s_num != num2:
        s_num -= 1
        s_idx -= 1
        s += 1
    s_idx_set = [s_idx, s] #작은수 좌표

    target = l_idx + l + s_idx + s - 1

    print(arr[target])
