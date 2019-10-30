import sys
sys.stdin = open('계산기_input.txt')

T = int(input())

operator = '+-*/.'


for tc in range(1, T+1):
    first_str = list(input().split())
    # print(first_str)
    stack = []
    num_cnt = 0
    oper_cnt = 0

    for i in range(len(first_str)):
        if first_str[i] not in operator: #숫자
            stack.append(int(first_str[i]))
            num_cnt += 1
            # print(stack)
        elif first_str[i] in operator: #연산자들
            oper_cnt += 1
            if first_str[i] == '.': #마지막
                if num_cnt == oper_cnt:
                    for s in stack:
                        print('#{} {}'.format(tc, s))
                else:
                    print('#{} {}'.format(tc, 'error'))
                    break

            else: # +-*/

                if len(stack) < 2:
                    print('#{} {}'.format(tc, 'error'))
                    break

                elif first_str[i] == '+':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    c = a + b
                    stack.append(c)
                elif first_str[i] == '*':
                    y = int(stack.pop())
                    x = int(stack.pop())
                    z = x * y
                    stack.append(z)
                elif first_str[i] == '-':
                    j = int(stack.pop())
                    i = int(stack.pop())
                    k = i - j
                    stack.append(k)
                elif first_str[i] == '/':
                    n = int(stack.pop())
                    m = int(stack.pop())
                    l = m // n
                    stack.append(l)


