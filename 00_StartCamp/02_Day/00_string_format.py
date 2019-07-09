#1. pyformat

name = '홍길동'
english_name = 'hong'

# print('안녕하세여.{}입니다. My name is{}'.format(name, english_name))
# print('안녕하세여.{1}입니다. My name is{0}'.format(name, english_name))
# print('안녕하세여.{1}입니다. My name is{1}'.format(name, english_name))

#2. f-strings

name = '홍길동'
print(f'안녕하세요, {name}입네다.')
# import random

# menu = ['김밥천국','스타박스','미군부대']

# lunch = random.choice(menu)
# print('오늘의 점심은 {}입니다.'.format(lunch))
# print(f'오늘의 점심은 {lunch}입니다.')
import random
numbers = list(range(1, 46))
lotto = random.sample(numbers, 6)
print(f'오늘의 행운 번호는 {sorted(lotto)}입니다.')

