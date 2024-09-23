from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


class main1(TemplateView):
    template_name = 'platform.html'

# class shop(TemplateView):
#     template_name = 'games.html'

class bascet(TemplateView):
    template_name = 'cart.html'

def menu(request):
    #mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    mydict=Game.objects.all().values()
    context={
         'mydict':mydict,
    }
    return render(request, 'games.html', context)

def sign_up_by_html(request):
    users=[]
    users1 = Buyer.objects.all().values()
    n_users=len(users1)
    for i in range(n_users):
        users.append(users1[i]['name'])
    # print(users)
    # print('Это покупатели', users)
    # users=['alex', 'max', 'vasy']
    info={}

    if request.method == 'POST':
        user_have=False
        username=request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if password==repeat_password:
            if age>=18:
                if is_user==False:
                    user_have=True
                else:
                    info['error'] = 'Пользователь уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error']='Пароли не совпадают'

        if user_have:
            message=(f'Приветствуем, {username}!')
            Buyer.objects.create(name=username, balance=0, age=age)
            # print(message)
            # users2 = Buyer.objects.all().values()
            # print('Это покупатели', users2)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)
# создаем forms.py  в приложении task5
def sign_up_by_django(request):
    users = []
    users1 = Buyer.objects.all().values()
    n_users = len(users1)
    for i in range(n_users):
        users.append(users1[i]['name'])
    # users=['alex', 'max', 'vasy']
    info={}

    if request.method == 'POST':
        user_have=False
        form = UserRegister(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if password==repeat_password:
                if age>=18:
                    if is_user==False:
                        user_have=True
                    else:
                        info['error'] = 'Пользователь уже существует'
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error']='Пароли не совпадают'

            if user_have:
                message=(f'Приветствуем, {username}!')
                Buyer.objects.create(name=username, balance=0, age=age)
                # print(message)
            else:
                message = info['error']
        return HttpResponse(message)
    else:
        form = UserRegister()
    info['form']=form
    return render(request, 'registration_page.html', info)

# {% list = mydict|setdefault('games') %}

# образец
# def index(request):
#      text= 1
#      name='vasy'
#      list=[1.0, 2.22, 3.3]
#      dict={'games': ['Atomic Heart", "Cyberpunk 2077"]}
#      context={
#          'text':text,
#          'name':name,
#          'list':list,
#      }
#      return render(request, 'index.html', context)

#   старый шаблон games
# {% block content %}
#     {% for key, value in mydict.items %}
#         {% for i in value %}
#             <p>{{ i }}<button>Купить</button> </p>
#         {% endfor %}
#     {% endfor %}
# {% endblock %}