def plus(n):
    global result

    if n == 0:
        return result
    else:
        result += n
        return

result = 0

print(plus(10))