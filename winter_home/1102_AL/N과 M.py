import sys
sys.stdin = open('N과 M.txt')

def bubble_sorted(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]> a[j]:
                a[i], a[j] = a[j], a[i]

def Per(n,m,temp):
    if n == m:
        result.append(temp[:])
    else:
        for i in range(len(data)):
            tem[m] = data[i]
            Per(n,m+1,tem)

a = list(map(int,input().split()))
data = list(map(int,input().split()))
result = []
sorted(result)
tem = [0 for _ in range(a[1])]
Per(a[1],0,tem)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j] , end=" ")
    print()