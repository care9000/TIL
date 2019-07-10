lunch = {
    '밀면': '054-000-0000',
    '뼈해장국': '054-484-4543',
    '대구알탕': '054-456-4562'
}

#1. 방법1

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        print(item)
        print(type(item))
        f.write(f'{item[0]}, {item[1]}\n')