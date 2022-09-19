from django.contrib import admin
# Importing Item from our models.py file
from .models import Item

# Register your models here.

admin.site.register(Item)
