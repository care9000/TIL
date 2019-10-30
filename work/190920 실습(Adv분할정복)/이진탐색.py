import sys
sys.stdin = open('이진_input.txt')

def binarysearch(t, l, r, cnt):

    global cnt_r, cnt_l, result

    m = (l+r)//2

    if t == A[m]:
        result += 1
        return

    elif t > A[m]: #오른쪽 탐색
        cnt_r = 1
        if (cnt == 0 or cnt == 2):
            l = m + 1
            binarysearch(t, l, r, cnt_r)

    elif t < A[m]: #왼쪽 탐색
        cnt_l = 2
        if (cnt == 0 or cnt == 1):
            r = m - 1
            binarysearch(t, l, r, cnt_l)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split())) # N개의 정수를 A에 저장
    B = list(map(int, input().split())) # 여기 M개의 정수에 대해 A에 있는지 이진 탐색
    A = sorted(A)
    testB = []
    result = 0

    # print(A)

    l = 0
    r = len(A) - 1


    for i in range(M):
        if B[i] in A:
            testB.append(B[i])

    # print(testB)

    if len(testB) == 0:
        result = 0

    else:
        for j in range(len(testB)):
            cnt_l = 0
            cnt_r = 0
            fail = 0
            binarysearch(testB[j], l, r, 0)


    print('#{} {}'.format(tc, result))