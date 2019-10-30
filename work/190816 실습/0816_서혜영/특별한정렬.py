import sys
sys.stdin = open('특별한정렬_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, len(arr)-1):
        max = i
        min = i
        if i % 2 == 0:
            for j in range(i+1, len(arr)):
                if arr[max] < arr[j]:
                    max = j
            arr[i], arr[max] = arr[max], arr[i]

        else:
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]

    arr = list(map(str, arr))
    arr = ' '.join(arr[0:10])
    print('#{} {}'.format(tc+1, arr))