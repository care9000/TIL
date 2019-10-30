#{1, 2, 3} 모든 부분 집합 출력하기

cnt = 0
N = 3
A = [0 for _ in range(N)] # 원소의 포함여부 저장(0,1)
data = [1, 2, 3]

def printSet(n):
    global cnt
    cnt += 1
    print("%d : " % (cnt), end='') # 생성되는 부분 배열의 갯수 출력

    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i] == 1:   # A[i]가 1이면 포함된 것이므로 출력
            print("%d " % data[i], end='')
    print()

def powerset(n, k):
    if n == k:          # Basis Part
        printSet(n)
    else:               # Inductive Part
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


powerset(N, 0)