import sys
sys.stdin = open('연산_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))

    num1 = max(data) # 큰수
    num2 = min(data) # 작은수

    arr = [0]
    a = 1
    cnt1 = 1
    while arr[-1] <= num1:
        arr.append(a)
        cnt1 += 1
        a = a + cnt1

    l_num = 0
    l_idx = 0
    l = 1
    for i in range(len(arr)):
        if arr[i] >= num1:
            l_num = arr[i]
            l_idx = arr.index(l_num)
            break

    while l_num != num1:
        l_num -= 1
        l_idx -= 1
        l += 1
    l_idx_set = [l_idx, l] #큰수 좌표


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

    total = l + l_idx + s + s_idx

    arr = [0]
    a = 1
    cnt2 = 1
    while len(arr) != total:
        arr.append(a)
        cnt2 += 1
        a = a + cnt2

    start_N = arr[-1]
    start_idx = total - 1
    sl = 1
    result = 0
    while start_idx != (l_idx + s_idx):
        start_N -= 1
        start_idx -= 1
        sl += 1

    result = start_N

    print('#{} {}'.format(tc, result))
