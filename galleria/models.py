from django.db import models


class Image(models.Model):
    category=models.CharField(max_length=20,null=True)
    title=models.CharField(max_length=20)
    description = models.CharField(max_length=20,blank=True)
    image_url=models.ImageField(upload_to='images/')

    @classmethod
    def allimages(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def search_image(cls,category):
        search=cls.objects.filter(category__icontains=category)
        return search