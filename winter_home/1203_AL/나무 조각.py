import sys
sys.stdin = open('나무 조각.txt')


def bubblesorted(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                for k in range(len(data)):
                    print(data[k], end=" ")
                print()


input_data = list(map(int, input() .split()))
bubblesorted(input_data)