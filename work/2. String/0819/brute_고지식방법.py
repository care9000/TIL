# text = "TTTTAACCA"
# pattern = "TTA"
# print(len(text)-len(pattern)+1)
#
# for i in range(len(text)-len(pattern)+1):
#     if text[i] == pattern[i]:
#         for j in range(i+1, len(pattern)):
#             if text[j+1] == pattern[j]:
#                 print('true')
#     else:
#         print('false')


def bruteForce2(text, pattern):
   for i in range(len(text)-len(pattern)+1):
       cnt = 0
       for j in range(len(pattern)):
           if text[i+j] != pattern[j]:
               break
           else: cnt += 1
       if (cnt >= len(pattern)) :
           return i
   return -1

text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(bruteForce2(text, pattern)))
print(text.find(pattern))


def BruteForce(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M  # 검색 성공
    else:
        return -1  # 검색 실패

p = "is"  # 찾을 패턴
t = "This is a book~!"
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이

print(BruteForce(p, t))
