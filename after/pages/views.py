from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request,'index.html')

# Template Variable 템플릿 변수
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick =random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def hello(request, name, age):
    name = {
        'name': name,
        'age': age,
    }


    return render(request,'hello.html', name)