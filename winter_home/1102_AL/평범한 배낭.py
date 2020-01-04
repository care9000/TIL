import sys
sys.stdin = open('평범한 배낭.txt')
#
def PowerSet(N, m, weight, value):
    global my_value
    if weight > K:
        return
    if N == m:
        # 만약 현재 가치가 원래 가치보다 더 클 경우
        if value > my_value:
            my_value = value
    else:
        # 물건 포함 시킬 경우
        PowerSet(N, m + 1, weight + info[m][0], value + info[m][1])
        # 물건 포함 시키지 않는 경우
        PowerSet(N, m + 1, weight, value)





N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
my_value = -1




PowerSet(N, 0, 0, 0)
print(my_value)