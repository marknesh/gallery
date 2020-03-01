from django.test import TestCase
from .models import Image


class ImageTestClass(TestCase):

    def setUp(self):
        self.image=Image(id=1,title="travel",description = "awsome",image_url="teval.com",pub_date="2000-03-01")


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))



# Create your tests here.
