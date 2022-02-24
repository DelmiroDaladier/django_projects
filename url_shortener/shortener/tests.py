from django.test import TestCase

# Create your tests here.
class UnitTestCase(TestCase):

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shortener/index.html') 
