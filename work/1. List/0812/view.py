import sys
sys.stdin = open('view_input.txt')

T = 10
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, len(arr)-2):
        compare = []
        for n in range(i-2, i+3):
            compare.append(arr[n])

        if compare[2] > compare[0] and compare[2] > compare[1] and compare[2] > compare[3] and compare[2] > compare[4]:
            a = compare[2]
            compare = sorted(compare)
            b = compare[-2]
            c = a - b
            ans += c

    print('#{} {}'.format(tc+1, ans))