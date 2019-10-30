nums = []
while True:
    num = int(input('숫자를 입력하세요.: '))

    if num < 100:
        nums = nums.append(num)
        print(nums)

    if num >= 100:
        res_sum = sum(nums)
        res_ave = res_sum / len(nums)
        print(res_sum)
        print(res_ave)
        break
