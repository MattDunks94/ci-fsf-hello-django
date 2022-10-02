# TestCase is an extension of the Python standard library module.
from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    # Testing the HTTP responses.
    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # Testing the '/add' view is equal to status code 200, successful reponse.
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # Testing the '/edit' view is equal to status code 200, successful reponse.
    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        # client is part of the django testing framework.
        # It acts as a 'dummy' browser.
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # def test_can_add_item(self):

    # def test_can_delete_item(self):

    # def test_can_toggle_item(self):
    
    
