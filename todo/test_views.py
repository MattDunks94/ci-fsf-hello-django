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

    # Testing adding item and redirects back to homepage('/').
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    # Testing deleting item.
    def test_can_delete_item(self):
        # Creating item with name.
        item = Item.objects.create(name='Test Todo Item')
        # Collecting item id.
        response = self.client.get(f'/delete/{item.id}')
        # Making sure it redirects to homepage.
        self.assertRedirects(response, '/')
        # Filtering through our Item database using item.id.
        existing_items = Item.objects.filter(id=item.id)
        # Testing whether the length of existing items is equal to 0.
        # Should equal 0 as we've deleted an item.
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create item with name and done status of True.
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Collecting the item id from /toggle path.
        response = self.client.get(f'/toggle/{item.id}')
        # Redirects back to homepage.
        self.assertRedirects(response, '/')
        # Getting item id.
        updated_item = Item.objects.get(id=item.id)
        # Checking whether the done status is False from our item.
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        # Create item.
        item = Item.objects.create(name='Test Todo Item')
        # Testing the path from our views to /edit, giving the item a name.
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # Testing the redirect back to homepage.
        self.assertRedirects(response, '/')
        # Collecting the item id.
        updated_item = Item.objects.get(id=item.id)
        # Checking if the item name is equal to the string.
        self.assertEqual(updated_item.name, 'Updated Name')

