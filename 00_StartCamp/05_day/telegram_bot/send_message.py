# 파이썬 코드로 텔레그램 메시지 보내기
from decouple import config
import requests


text = '삼성 드가고 싶다.'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)
