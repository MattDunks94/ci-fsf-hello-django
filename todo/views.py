from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    # This will be displayed on the browser.
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # Receives user data, new item, and adds it to Item class
    if request.method == "POST":
        name = request.POST.get("item_name")
        done = "done" in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    # This will be displayed on the browser.
    return render(request, 'todo/add_item.html')