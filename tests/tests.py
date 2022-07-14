import django
from unittest import TestCase
from django.test import Client

class TestHomeBlogs(TestCase):
    def test_home_blog_avaleable(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
