#{1, 2, 3} 모든 부분 집합 출력하기
total = 0
cnt = 0
N = 10
A = [0 for _ in range(N)] # 원소의 포함여부 저장(0,1)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n, current_sum):
    result = 0
    for i in range(n):
        if A[i] == 1:
            result += data[i]

    if result == 10:
        for j in range(n):
            if A[j] == 1:
                print('%d ' % data[j], end='')
        print()


def powerset(n, k, current_sum):
    global total

    ########################################
    if current_sum > 10:
        return
    ########################################

    total += 1
    if n == k:          # Basis Part
        printSet(n, current_sum)

    else:               # Inductive Part
        A[k] = 1

        powerset(n, k+1, current_sum + data[k])

        # for i in range(len(A)):
        #     if A[i] == 1:
        #         current_sum += data[i]
        # powerset(n, k+1, current_sum)

        A[k] = 0

        powerset(n, k + 1, current_sum)
        # for i in range(len(A)):
        #     if A[i] == 1:
        #         current_sum += data[i]
        # powerset(n, k+1, current_sum)

powerset(N, 0, 0)
print('호출회수 : {}'.format(total))