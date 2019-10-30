# num = int(input('숫자를 입력하시오.: '))
# # num = 456789 #babygin 확인할 6자리 수
# c = [0] * 12 #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
#
# for i in range(6):
#     c[num % 10] += 1
#     num //= 10
#
# print(c)

# arr = [1, 2, 4, 7, 8, 3]
arr = [6, 6, 6, 7, 7, 7]

def babygin():
   global flag

   check = 0

   if arr[0] == arr[1] and arr[1] == arr[2]:
       check += 1
   if arr[3] == arr[4] and arr[4] == arr[5]:
       check += 1

   if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
       check += 1
   if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
       check += 1

   if check == 2:
       flag = 1
       return



def perm(n, k):
    if k == n:
        babygin()

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


flag = 0
perm(6, 0)

if flag:
    print('babygin!')
else:
    print('응 아니야.')
