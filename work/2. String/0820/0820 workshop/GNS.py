import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(str, input().split())
    arr = list(map(str, input().split()))

    sorted_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    test_dict = {}

    for char in arr:
        if char not in test_dict:
            test_dict[char] = 1
        else:
            test_dict[char] += 1

    result = []
    for a in sorted_list:
        for _ in range(test_dict[a]):
            result.append(a)

    zzz = ' '.join(result)
    print('{} {}'.format(N, zzz))
