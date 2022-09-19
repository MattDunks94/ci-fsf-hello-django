from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    # This will be displayed on the browser.
    return render(request, 'todo/todo_list.html', context)