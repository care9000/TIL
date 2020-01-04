import sys
sys.stdin = open('11052_카드_구매하기.txt')




N = int(input())

dummy = list(map(int, input().split()))

P = [0]
P += dummy


for i in range(2, len(P)):
    for j in range(1, i):
        if i % j == 0:
            if P[j] * (i / j) >= P[i]:
                P[i] = P[j] * (i // j)
        if P[i] < P[j] + P[i - j]:
            P[i] = P[j] + P[i - j]




max_price = 0

A = [0] * N
info = []
print(P[-1])
