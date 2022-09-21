from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]

def creator(request):
    return HttpResponse(f'<h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>{author["surname"]} {author["name"][0]}. {author["thirdname"][0]}.</i>')

def main_page(request):
    return render(request, 'main.html')

def about(request):
    author = {
        "name": "Константин",
        "surname": "Кондрашов",
        "email": "kondrashov.konstantin@mail.ru"
    }
    return HttpResponse(str(author))

def item(request, item_id):
    for item in items:
        if item["id"] == item_id:
            return HttpResponse(f'Товар {item["id"]}: {item["name"]}, кол-во {item["quantity"]}')
    else:
        return HttpResponseNotFound(f"Item with id {item_id} not found")

def get_items(request):
    # result = "<ol>"
    # for item in items:
    #     result += f"<li> <a href = 'item\{item['id']}'> {item['name']} </a> </li>"
    # result += "</ol>"
    # return HttpResponse(result)

    context = {
        "items" : items
    }
    return render(request, "items_list.html", context)


