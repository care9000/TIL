# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자.

data=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
a='0F97A3'
result=""
for i in range(len(a)):
    if '0' <= a[i] <= '9':
        result += (data[int(a[i])])
    else:
        if a[i] == "A":
            result += (data[10])
        if a[i] == "B":
            result += (data[11])
        if a[i] == "C":
            result += (data[12])
        if a[i] == "D":
            result += (data[13])
        if a[i] == "E":
            result += (data[14])
        if a[i] == "F":
            result += (data[15])

for i in range(len(result)//7):
   n = 0
   for j in range(i*7, i*7+7, 1):
       n = n * 2 + int(result[j])
   print(n, end=' ')

a = len(result) - (len(result)//7*7)

if len(result) % 7 != 0:
   n = 0
   for j in range(len(result)//7*7, len(result), 1):
       n = n * 2 + int(result[j])
   print(n, end=" ")
print()


# def aToh(c):
#     if c <= '9':
#         return ord(c) - ord()
#         return ord(c) - ord('A') + 10
