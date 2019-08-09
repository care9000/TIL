from django.shortcuts import render
import random
from datetime import datetime
import requests
# 1. 기본 로직.
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def images(request):
    return render(request, 'pages/images.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    menu = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menu)    
    context = {
        'name': name, 
        'age': age,
        'pick': pick,
    }
    return render(request, 'pages/hello.html', context)


#4. 실습

#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기 소개 페이지
def hi(request, name, age):
 
    context = {
        'name': name, 
        'age': age,
    }
    return render(request, 'pages/hi.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def mul(request, n1, n2):
    
    mul = {
        'n1': n1,
        'n2': n2,
        'n3': n1*n2
    }
    return render(request, 'pages/mul.html', mul)



#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle(request, r):
    result= {
        'r': r,
        'area': r**2*3.141592
    }
    return render(request, 'pages/circle.html', result)

#5. DTL(Django Temlpate Langage)
def template_language(request):
    menus = ['짜장면', '탕수육', '양장피', '짬뽕']
    my_sentence ='Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = ['apple']

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)


#6. 실습
#6-1. isbirth
def isbirth(request):
    today= datetime.now()
    day1 = today.day
    month1 = today.month
    if day1 == 28 and month1 == 9:
        result = True
    else:
        result = False
    context = {
        # 'today':today,
        # 'day1':day1,
        # 'month':month1,
        'result':result
    }

    return render(request,'pages/isbirth.html', context)

#6-2. 회문판별
def pal(request,name):
    if name == name[::-1]:
        result = True
    else :
        result = False
    
    context ={
        'name':name,
        'result':result,
    }

    return render(request,'pages/pal.html',context)

def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos =list(random.sample(range(1, 46), 6))
    

    context ={
        'real_lottos': real_lottos,
        'lottos': sorted(lottos),
    }

    return render(request, 'pages/lotto.html', context)



#7. Form - GET
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context ={
        'message': message,
        'message2': message2,
        
    }
    return render(request,'pages/catch.html', context)


def ping(request):
    return render(request,'pages/ping.html')

def pong(request):
    message1 = request.GET.get("message1")
    message2 = request.GET.get("message2")
    context ={
        'message1' :message1,
        'message2':message2,
    }
    return render(request,'pages/pong.html',context)
    

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get("word")
    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font라는 변수에 저장.
    font = random.choice(fonts)
    #5. 위에서 사용자에게 받은  word와 font를 가지고 다시 요청을 보낸다. 그리고 응답결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context={
        'result' : result
    }
    return render(request,'pages/result.html',context)

#9. Form -POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context ={
        'name':name,
        'password':pwd,
    }
    return render(request, 'pages/user_create.html', context)


#10. 정적 파일
def static_example(request):
    return render(request,'pages/static_example.html')

