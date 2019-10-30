import sys
sys.stdin = open('동철_input.txt')


def perm(n, k, cur_per):
    global max_value

    if cur_per <= max_value:
        return

    if k == n:
        if cur_per > max_value:
            max_value = cur_per

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cur_per * ((data[k][arr[k]])/100))
            arr[k], arr[i] = arr[i], arr[k] # 다시 제자리로 돌려놔야한다.



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    # print(arr)
    max_value = 0
    perm(N, 0, 1)
    # print(max_value)
    # num = round(max_value * 100, 7)
    print('#%d %.6f' %(tc, max_value*100))