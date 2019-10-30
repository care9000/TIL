import sys
sys.stdin = open('입력_input.txt')

T = input()
a, b = map(int, input().split())

data = [input() for _ in range(a)]

print(T)
print(a, b)
[print(data[i]) for i in range(a)]