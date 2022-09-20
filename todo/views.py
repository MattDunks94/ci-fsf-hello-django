from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    # The get_object_or_404 method returns a class if it exists.
    # In this case, collecting our Item class, as first parameter.
    # Second parameter is our item_id from todo_list.html, button.
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        # Instance accesses the objects within a class (Item)
        # This pre-populates the form with the current item details
        form = ItemForm(request.POST, instance=item)
        # is_valid() method runs validation, returns a boolean
        # If it returns TRUE it saves user data
        if form.is_valid():
            # save() saves the form data into Item, the model, forms.py
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)