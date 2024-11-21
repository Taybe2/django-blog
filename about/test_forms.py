from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_name_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")
    
    def test_email_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'taybe',
            'email': 'test',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")
    
    def test_message_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'taybe',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")
