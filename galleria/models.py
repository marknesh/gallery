from django.db import models


class Category(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.location

class Image(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,default=None)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=20)
    description = models.CharField(max_length=20,blank=True)
    image_url=models.ImageField(upload_to='images/')
    pub_date=models.DateField(auto_now_add=True)





    @classmethod
    def allimages(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def search_image(cls, category):
        search = cls.objects.filter(category=category)
        return search

    @classmethod
    def filter_image(cls, location):
        location = cls.objects.filter(location=location)
        return location








