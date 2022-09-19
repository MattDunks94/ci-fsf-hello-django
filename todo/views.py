from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    # This will be displayed on the browser.
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        # Assigning variable to our ItemForm class from forms.py
        form = ItemForm(request.POST)
        # is_valid() method runs validation, returns a boolean
        # If it returns TRUE it saves user data
        if form.is_valid():
            # save() saves the form data into Item, the model, forms.py
            form.save()
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }
    # This will be displayed on the browser.
    return render(request, 'todo/add_item.html', context)