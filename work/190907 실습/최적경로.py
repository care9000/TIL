import sys
sys.stdin = open('경로_input.txt')

def printArr(n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

def calc(n):
    result = []
    for i in range(n):
        result.append(arr[i])



def perm(n, k):
    if k == n:
        calc(n)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k] # 다시 제자리로 돌려놔야한다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    hnc = [] # 집, 회사
    arr = [i for i in range(N)]
    min = 9874563

    for i in range(4):
        hnc.append(data.pop(0))

    perm(N, 0)
    # print(data)
    # print(hnc)
    print(arr)
    # for i in range(N):

