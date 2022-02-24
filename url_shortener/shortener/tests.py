import uuid

from .models import Url
from django.test import TestCase
from .view_helpers import create as create_helper

# Create your tests here.
class UnitTestCase(TestCase):

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shortener/index.html') 
    
    def save_url(self):
        link = 'http://www.example.com'
        link = create_helper.remove_http(link)
   
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()

        return new_url

    def test_url_object(self):
        url = self.save_url()
        pulled_url = Url.objects.get(link='www.example.com')
        self.assertEqual(url.link, pulled_url.link)

