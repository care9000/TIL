while True:
    num = int(input())
    if num == -1:
        break
    if num % 3 >= 1:
        continue
    if not num % 3:
        result = num // 3
        print(result)
