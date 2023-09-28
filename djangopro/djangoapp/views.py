from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

from django.template.response import TemplateResponse
def python(request):
    return render(request, "djangoapp/python.html")

def sample_id(request):
    return render(request, "djangoapp/sample.html")

def index(request):
    return render(request, 'djangoapp/index.html')

def about(request):
    return render(request,'djangoapp/about.html')

def contacts(request):
    return render(request,'djangoapp/contacts.html')

def user_id(request, name,id):
    return HttpResponse(f"<h2>Имя: {name}</h2> <h2>ID: {id}</h2>")

def user(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")

def testsample(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "djangoapp/testsample.html", context=data)

def username(request,name,age):
    if name == 'Alex' and age ==15:
        return HttpResponse(f'Добро пожаловать  ,Ваше имя {name} Ваш возраст{age} ')
    else:
        return HttpResponse(f'Пользователь с именем {name} еще не авторизирован')

def time(request):
    #data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "djangoapp/time.html")
m = random.randrange(1, 100)
def random_num(request):
    global m
    data = {'m': m}
    return render(request, 'djangoapp/random_num.html', context=data)

def winner(request):
    win_num = [6, 72, 33, 12, 93]
    data = {'m':m}
    return render(request , 'djangoapp/winners.html', context={'win_num': win_num, 'data':data})

def lang(request):
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    return render(request, "djangoapp/lang.html", context={"langs": langs})
# def username(request):
#     age = request.GET.get("age")
#     name = request.GET.get("name")
#     return HttpResponse(f"<h2>Добро пожаловать Имя: {name}  Возраст: {age}</h2>")

def products(request):
    return HttpResponse("Список товаров")


def new(request):
    return HttpResponse("Новые товары")


def top(request):
    return HttpResponse("Наиболее популярные товары")


def products_id(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def characteristics(request, id):
    return HttpResponse(f"Характеристики о товаре {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")


def form(request):
    return render(request, "djangoapp/form.html")


def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")