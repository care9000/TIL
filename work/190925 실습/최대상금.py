import sys
sys.stdin = open('최대상금_input.txt')

def Result(A):
    global max_bonus

    num = ''
    for i in range(len(A)):
        num += str(A[i])

    if int(num) > max_bonus:
        max_bonus = int(num)

def perm(n, k, a):
    if k == int(c): # depth가 c
        Result(a)
        # 하고싶은 일
    else:
        for i in range(0, n-1):
            for j in range(i+1, n):
                A[i], A[j] = A[j], A[i]
                perm(n, k+1, A)
                A[i], A[j] = A[j], A[i]


T = int(input())

for tc in range(1, T+1):
    sample, c = map(str, input().split()) # sample 은 str 숫자 , c 는 str 횟수
    n = len(sample) # sample 길이 int

    # print(sample)

    A = [int(i) for i in sample]

    # 가지치기
    c = int(c)
    if c > 5:
        if c % 2 == 0:
            c = 4
        else:
            c = 5

    max_bonus = 0
    perm(n, 0, A)

    print('#{} {}'.format(tc, max_bonus))