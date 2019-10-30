n = input()
arr = []

for i in n.split():
    arr = arr.append(int(i))

for num in arr:
    mul_3 = 0
    mul_5 = 0
    if not num % 3:
        mul_3 += 1
    elif not num % 5:
        mul_5 += 1

print('Multiples of 3 : {}'.format(mul_3))
print('Multiples of 5 : {}'.format(mul_5))