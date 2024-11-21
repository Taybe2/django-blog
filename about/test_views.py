from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(
            title="About me", profile_image="placeholder",
            content="Some content", updated_on=datetime.now())
        self.about.save()
    
    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Some content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for requesting collaboration form"""
        post_data = {
            'name': 'Taybe',
            'email': 't@gmail.com',
            'message': 'Let\'s collaborate!'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )