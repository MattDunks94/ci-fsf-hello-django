from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    # This will be displayed on the page.
    return render(request, 'todo/todo_list.html')