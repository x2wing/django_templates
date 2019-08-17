from django.shortcuts import render #импорт функции
# Create your views here.
def index(request):#создаем свою функцию
    context = {}#с помощью словаря можем передать модель и форму в шаблон HTML
    return render(request, 'blog/index.html', context)#собственно вызываем шаблон HTML

