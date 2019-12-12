import sys
sys.stdin = open('N과 M (4).txt')

def Pem(n, m, sum):
    if n == m:
        if sum not in result:
            result.append(sum)
    else:
        for i in range(0, len(data)):
            Pem(n, m+1, sum + str(data[i]))
N, M = map(int, input().split())
data = [i for i in range(1, N + 1)]
result = []
Pem(M, 0, "")
re = []
for i in range(len(result)):
    re.append(result[i])
