# TestCase is an extension of the Python standard library module.
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # Simulating users input, being empty, no input.
        form = ItemForm({'name': ''})
        # This should be invalid, assertFalse checks the validation.
        self.assertFalse(form.is_valid())
        # Asserts whether or not there's a name key in the dictionary
        # of form errors.
        self.assertIn('name', form.errors.keys())
        # Checks if error message is the one mentioned.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Assigning the form a test item.
        form = ItemForm({'name': 'Test Todo Item'})
        # Testing valid status, should be valid.
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # Assigning form an empty form.
        form = ItemForm()
        # Checks the fields in our form are explicitly 'name', 'done'.
        # This prevents any changes we dont want to be displayed.
        # Also prevents it from being reordered.
        self.assertEqual(form.Meta.fields, ['name', 'done'])

