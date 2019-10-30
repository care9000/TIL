
def pre(T): # 전위
    if T:
        print('{}'.format(T), end=" ")
        pre(tree[T][0])
        pre(tree[T][1])

def cen_pre(T): # 중위
    if T !=0:
        cen_pre(tree[T][0])
        print('{}'.format(T), end=" ")
        cen_pre(tree[T][1])

def post_pre(T): # 후위
    if T !=0:
        post_pre(tree[T][0])
        post_pre(tree[T][1])
        print('{}'.format(T), end=" ")

import sys
sys.stdin = open('트리_input.txt')

v = int(input())
data = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(v+1)]

for i in range(0, len(data), 2):
    if tree[data[i]][0] == 0:
        tree[data[i]][0] = data[i+1]
        tree[data[i+1]][2] = data[i]
    else:
        tree[data[i]][1] = data[i+1]
        tree[data[i+1]][2] = data[i]

[print(tree[i]) for i in range(len(tree))]


pre(1)
print()
cen_pre(1)
print()
post_pre(1)