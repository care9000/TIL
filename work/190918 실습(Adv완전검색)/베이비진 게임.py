import sys
sys.stdin = open('베이비진_input.txt')

def game(arr):
    global result

    A = sorted(arr)

    for i in range(len(arr)-2):
        if A[i] == A[i+1] and A[i+1] == A[i+2]:
            result += 1




T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    print(cards)

    user1 = []
    user2 = []
    result = 0
    flag = 0

    for i in range(0, len(cards), 2):
        user1.append(cards[i])
        if len(user1) >= 3:
            game(user1)
            if result == 1:
                flag = 1

        if len(user2) >= 3:
            game(user2)
            if result == 1:
                flag = 2

    print(flag)