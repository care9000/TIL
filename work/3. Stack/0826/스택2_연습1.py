# contents = input('수식을 입력하세요.: ')
#
# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# result = []
# temp = []
#
# for i in contents:
#     if i in nums:
#         result.append(i)
#     else:
#         temp.append(i)
#
# a = temp[::-1]
#
# b = ' '.join(result)
# c = ' '.join(a)
#
# print(b, end=' ')
# print(c)

stack = []
str = '2+3*4/5'
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(len(str)):
    if str[i] not in nums:
        stack.append(str[i])

    else:
        print(str[i], end='')

while len(stack) != 0:
    print(stack.pop(), end='')