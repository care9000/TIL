def power(base, exponent):
    if base == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= base

    return result

print(power(2, 10))