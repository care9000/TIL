import sys
sys.stdin = open('N과 M (2).txt')

def bubblesorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

def Pem(n, m):
    if n == m:
        a = data[:M]
        bubblesorted(a)
        if a not in result:
            result.append(a[:])
    else:
        for i in range(m, len(data)):
            data[i], data[m] = data[m], data[i]
            Pem(n, m+1)
            data[i], data[m] = data[m], data[i]

N, M = map(int, input().split())
data = [i for i in range(1, N + 1)]
result = []
Pem(M, 0)
re = []
for i in range(len(result)):
    tmp = []
    for j in range(len(result[i])):
        tmp.append(str(result[i][j]))
    re.append(' '.join(tmp))
print('\n'.join(re))
