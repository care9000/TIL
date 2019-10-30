def BubbleSort(a): #정렬한 List
    for i in range(len(a)-1, 0, -1): #범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

# def test():
#     global a
#     a = 500
#     print(a) # 읽기
#
# a = 100 # 값형
# test()
# print(a)

data = [55, 7, 78, 12, 42] # 참조형, 주소를 가지고 있음. 전역변수처럼 사용. 변경 가능
BubbleSort(data)
print(data)