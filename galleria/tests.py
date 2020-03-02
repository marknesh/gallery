from django.test import TestCase
from .models import Image


class ImageTestClass(TestCase):

    def setUp(self):
        self.image=Image(id=1,title="travel",description = "awsome",image_url="teval.com",pub_date="2000-03-01")


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def test_save_method(self):
        self.image.save_image()
        IMage = Image.objects.all()
        self.assertTrue(len(IMage) > 0)

    def test_delete_method(self):
        self.image.delete_image()
        Imaage=Image.objects.all()
        self.assertTrue(len(Imaage)<1)






# Create your tests here.
