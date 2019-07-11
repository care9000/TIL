from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    num = request.args.get('num')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(num))
    lotto = res.json() #로또 결과(딕셔너리)
    


    #1. 번호 6개 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto['drwtNo{}'.format(i)])
        
    #2. 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))

    if len(numbers) == 6:
        #번호 교집합 개수 찾기
        matched = 0 
        for num in numbers:
            if num in winner:
                matched += 1
        if matched == 6:
            result = '1등입니다!!(강남아파트)'
        elif matched == 5:
            if lotto['bnusNo'] in numbers:
                result = '2등입니다!!.(그랜져한대)'
            else:
                result = '3등입니다!!(휴대폰한대)'
        elif matched == 4:
            result = '4등입니다.(로또*10장)'
        elif matched == 3:
            result ='5등입니다.(쭈쭈바*5)'
        else:
            result = '꽝입니다.(동행복권 개이득)'

    else:
        result = '번호의 수가 일치하지 않습니다.'        
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)