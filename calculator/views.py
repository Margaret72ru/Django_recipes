from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'gintonic': {
        'джин, мл': 100,
        'содовая, мл': 300,
        'лёд, кусок': 2,
        'лимон, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_page(request):
    text = ""
    for item in DATA.keys():
        text = text + "<br>" + item
    return HttpResponse("Кулинарная книга" + text)


def get_recipe(request, page):
    context = {'recipe': {}}
    rec_item = str(page).lower()

    if DATA.keys().__contains__(rec_item):
        serv_count = 1
        if request.GET.keys().__contains__("servings"):
            try:
                serv_count = int(request.GET["servings"])
            except ValueError:
                serv_count = 1

        item = DATA[rec_item]
        for i in item.keys():
            context['recipe'][i] = item[i] * serv_count

    return render(request, 'calculator/index.html', context)
