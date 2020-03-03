from django.db import models
import pyperclip


class Category(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.location

class Image(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=20)
    description = models.CharField(max_length=20,blank=True)
    image_url=models.ImageField(upload_to='images/')
    pub_date=models.DateTimeField(auto_now_add=True)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def copy_image(self,image_url):
        pyperclip.copy(image_url)

    def paste_image(image_url):
        pyperclip.paste()


    @classmethod
    def allimages(cls):
        images=cls.objects.all()
        return images



    @classmethod
    def search_image(cls, category):
        search = cls.objects.filter(category__category=category)
        return search

    @classmethod
    def filter_image(cls, location):
        location = cls.objects.filter(location__location=location)
        return location








