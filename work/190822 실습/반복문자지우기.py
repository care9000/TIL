import sys
sys.stdin = open('반복문자_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    compare = []

    for i in range(len(arr)):
        if len(compare) == 0:
            compare.append(arr[i])

        elif len(compare) != 0:
            if compare[-1] != arr[i]:
                compare.append(arr[i])

            elif compare[-1] == arr[i]:
                compare.pop()

    print('#{} {}'.format(tc, len(compare)))



