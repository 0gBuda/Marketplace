from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()


    context = {
        'content': "Магазин мебели HOME",
        'categories': categories
    }

    return render(request, 'main/index.html', context)


