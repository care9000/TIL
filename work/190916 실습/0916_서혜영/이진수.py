import sys
sys.stdin = open('이진수_input.txt')

T = int(input())

data=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

for tc in range(1, T+1):
    N, nums = map(str, input().split())
    result = ""
    # print(N, nums)
    for i in range(len(nums)):
        if '0' <= nums[i] <= '9':
            result += (data[int(nums[i])])
        else:
            if nums[i] == "A":
                result += (data[10])
            if nums[i] == "B":
                result += (data[11])
            if nums[i] == "C":
                result += (data[12])
            if nums[i] == "D":
                result += (data[13])
            if nums[i] == "E":
                result += (data[14])
            if nums[i] == "F":
                result += (data[15])

    print('#{} {}'.format(tc, result))