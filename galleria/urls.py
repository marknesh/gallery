from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.welcome,name="home" ),
    re_path(r'^image/(\d+)',views.image,name='image'),
    re_path(r'^search/image/(\d+)', views.image, name='image'),
    re_path(r'^filter/image/(\d+)', views.image, name='image'),
    path('search/', views.search, name='search'),
    path('filter/', views.location, name='location'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)