"""
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 만드시오.
"""

# str = input('문자를 입력하세요: ')

# print(f'첫글자는 {str[0]}입네다.')
# print(f'마지막글자는 {str[-1]}입네다.')
"""
문제2. 자연수 n이 주어질 떄, 1부터 n까지 한 줄에 하나씩 출력하는 프로그램을 만드세요.
"""
# a = int(input("입력해~~주세여: "))
# for i in range(1,a+1):
#     print(i)
"""
문제3. 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하세요.
"""

# number = int(input('숫자를 입력해~~~주세요: '))

# for i in range(1,number+1):
# if number %2==0:
#     print("{}는 짝수입네다.".format(number))
# else :
#     print("{}는 홀수입네다.".format(number))
"""
문제4. 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과,
과학은 80점 이상일 때 합격이라고 정했습니다.
(한과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격하면 True, 북합격이면 False가 출력되도록 작성하세여.
"""

# a = int(input('국어: '))
# b = int(input('영어: '))
# c = int(input('수학: '))
# d = int(input('과학: '))

# if a>=90 and b>80 and c>85 and d>=80:
#     print("지원자는 저희 YG에서 캐스팅하겠습니다.")

# else :
#     print("지원자는 저희 YG 와 함께 할 수 없습니다.")
   

"""
문제5. 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된 가격을 높은 가격순으로 한줄에
하나씩 출력하는 프로그램을 만드세요.
입력예시: 30000;2000;40000
출력예시
40000
30000
2000
"""
prices = input('물품 가격을 입력하세요: ')

makes = prices.split(';')
boxs = []

# print(boxs)
# print(type(makes))
for make in makes:
    boxs.append(int(make))

boxs.sort(reverse=True)

for box in boxs:
    print(box)
