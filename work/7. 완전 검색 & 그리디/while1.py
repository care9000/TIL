i = 0 # 조건 초기화
while i < 10: # 조건식
    print(i)
    i += 1 # 증감
print(i)
print()

###############################################

for i in range(10):
    print(i)
    i += 3
print(i)
print()

###############################################

i = 100 # 조건 초기화
while True: # 조건식
    print(i)
    i += 1 # 증감
    if i >= 10:
        break
print(i)