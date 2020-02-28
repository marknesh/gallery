from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.welcome,name="DD" ),
    re_path(r'^image/(\d+)',views.image,name='article'),
    path('search/', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)