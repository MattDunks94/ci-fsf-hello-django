# TestCase is an extension of the Python standard library module.
from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    # Testing the done status is False as default.
    def test_done_defaults_to_false(self):
        # Creating new 'dummy' item with name.
        item = Item.objects.create(name='Test Todo Item')
        # Checking whether the done status is False.
        self.assertFalse(item.done)

