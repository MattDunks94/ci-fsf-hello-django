from django.db import models

# Create your models here.


# 'name' and 'done' are our input fields for our form.
class Item(models.Model):
    # CharField(), imported from models, text only method.
    # max_length set to 50 characters.
    # null and blank makes sure the name field is not empty.
    name = models.CharField(max_length=50, null=False, blank=False)
    # BooleanField(), imported from models, is either TRUE or FALSE.
    # default sets the item to not done, TRUE meaning it's done.
    # Displays checkbox.
    done = models.BooleanField(null=False, blank=False, default=False)
    # Overiding django string method, displaying own item name.
    def __str__(self):
        return self.name
