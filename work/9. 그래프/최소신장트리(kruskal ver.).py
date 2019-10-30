import sys
sys.stdin = open('최소신장트리_input.txt')

def Find_Set(x):
    if x == PI[x]:
        return x
    else:
        return Find_Set(PI[x])

def Union(x, y):
    PI[Find_Set(x)] = Find_Set(y)


def MST_KRUS():
    cnt = 0
    total = 0

    for j in range(len(data)):
        a = data[j][0]
        b = data[j][1]

        if Find_Set(a) != Find_Set(b):
            cnt += 1
            total += data[j][2]
            Union(a, b)

            if cnt == V:
                return total



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 마지막 노드번호(V), 간선의 개수(E)
    data = [list(map(int, input().split())) for _ in range(E)]
    # n1, n2, w(가중치)

    # 예 저도 써봤습니다. 람다
    data.sort(key=lambda x : x[2])

    PI = list(range(V+1))

    a = MST_KRUS()

    print('#{} {}'.format(tc, a))

