from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# def main_page(request):
#     return HttpResponse("Hello")




author = {
        "name": "Константин",
        "surname": "Кондрашов",
        "email": "kondrashov.konstantin@mail.ru",
        "phone": "89955095643",
        "thirdname": "Юрьевич"
    }

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 4, "name": "Картофель фри" ,"quantity":0},
#    {"id": 5, "name": "Кепка" ,"quantity":124},
# ]

title = "Добро пожаловать!"

def main_page(request):
    items = Item.objects.all()
    context = {
        "items" : items,
        "title" : title
    }
    return render(request, "main.html", context)
    # return render(request, 'main.html')


def items_list(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "items_list.html", context)


def item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except:
        raise ObjectDoesNotExist
    context = {
        "item" : item,
        "title" : title,
        "item_id" : item_id
    }
    return render(request, 'item.html', context)


def about(request):
    author = {
        "name": "Константин",
        "surname": "Кондрашов",
        "email": "kondrashov.konstantin@mail.ru"
    }
    return HttpResponse(str(author))


