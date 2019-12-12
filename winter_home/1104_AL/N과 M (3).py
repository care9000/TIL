import sys
sys.stdin = open('N과 M (3).txt')

def bubblesorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def Pem(n, m, sum):
    if n == m:
        result.append(sum)
    else:
        for i in range(0, len(data)):
            data[i]
            Pem(n, m+1,sum + str(data[i]) +(' '))

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
result = []
Pem(M, 0,'')
re = []
for i in range(len(result)):
    re.append(result[i])
print('\n'.join(re))