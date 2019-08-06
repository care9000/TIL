from django.shortcuts import render
import random
from datetime import datetime
# 1. 기본 로직.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def images(request):
    return render(request, 'images.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)


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
    return render(request, 'hello.html', context)


#4. 실습

#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기 소개 페이지
def hi(request, name, age):
 
    context = {
        'name': name, 
        'age': age,
    }
    return render(request, 'hi.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def mul(request, n1, n2):
    
    mul = {
        'n1': n1,
        'n2': n2,
        'n3': n1*n2
    }
    return render(request, 'mul.html', mul)



#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle(request, r):
    result= {
        'r': r,
        'area': r**2*3.141592
    }
    return render(request, 'circle.html', result)

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
    return render(request, 'template_language.html', context)


#6.project
def info(request):
    return render(request, 'info.html')

#7.project -2
def student(request,name):
    context = {
        'name': name,
    }
    return render(request, 'student.html', context)