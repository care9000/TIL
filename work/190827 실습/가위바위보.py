import sys
sys.stdin = open('가위바위보_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    person = list(map(int, input().split()))

    print(N)
    print(person)
    n = (N//2)
    print(n)
    team1 = []
    team2 = []
    for i in range(n, N):
        team2