from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.category




class Image(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=20)
    description = models.CharField(max_length=20,blank=True)
    image_url=models.ImageField(upload_to='images/')




    @classmethod
    def allimages(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def search_image(cls,category):
        search=cls.objects.filter(Category=category)
        return search

