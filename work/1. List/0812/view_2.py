import sys
sys.stdin = open('view_input.txt')

T = 10
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, len(arr)-2):
        a = arr[i]
        if a > arr[i-2] and a > arr[i-1] and a > arr[i+1] and a > arr[i+2]:
            compare = [arr[i-2], arr[i-1], a, arr[i+1], arr[i+2]]
            compare = sorted(compare)
            b = a - compare[-2]
            ans += b
    print('#{} {}'.format(tc + 1, ans))