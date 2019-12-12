import sys
sys.stdin = open('N과 M (1).txt')

def bubblesorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def Pem(n, m, sum):
    if n == m:
        result.append(sum)
    else:
        for i in range(m, len(data)):
            data[i], data[m] = data[m], data[i]
            Pem(n, m+1,int(str(sum)+str(data[m])))
            data[i], data[m] = data[m], data[i]

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
result = []
Pem(M, 0, 0)
bubblesorted(result)
re = []
for i in range(len(result)):
    re.append(str(result[i]))
for i in range(len(re)):
    for j in range(len(re[i])):
        print(re[i][j],end=" ")
    print()
