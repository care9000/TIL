import sys
sys.stdin = open('괄호_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    target = ['{', '}', '(', ')']
    compare = []

    for i in range(len(arr)):
        if arr[i] in target:
            if arr[i] == '{' or arr[i] == '(':
                compare.append(arr[i])

            elif arr[i] == '}' or arr[i] == ')':
                if len(compare) == 0:
                    compare.append(0)
                    break

                elif arr[i] == target[1]:
                    if compare[-1] == target[0]:
                        compare.pop()
                    else:
                        compare.clear()
                        compare.append(0)
                        break
                elif arr[i] == target[3]:
                    if compare[-1] == target[2]:
                        compare.pop()
                    else:
                        compare.clear()
                        compare.append(0)
                        break

    if len(compare) == 0:
        compare.append(1)
    elif len(compare) != 0:
        compare.clear()
        compare.append(0)



    print('#{} {}'.format(tc, compare[0]))