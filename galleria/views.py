from django.shortcuts import render,Http404
from .models import Image

def welcome(request):
    image=Image.allimages
    return render(request,'pictures/home.html',{'image':image})
def image(request,image_id):

    ss=Image.copy_image
    try:
        imageid= Image.objects.get(id = image_id)

    except Exception:
        raise Http404()
    return render(request,"pictures/image.html", {"imageid":imageid,"ss":ss})

def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search=request.GET.get("category")
        searched=Image.search_image(search)
        message=f"{search}"
        return render(request,'pictures/search.html',{"message": message, "searched": searched})
    else:
        message = "since you haven't searched for any term"
        return render(request, 'pictures/search.html', {"message": message})


def location(request):
    if 'location' in request.GET and request.GET["location"]:
        search=request.GET.get("location")
        searched=Image.filter_image(search)
        message=f"{search}"
        return render(request,'pictures/filter.html',{"message": message, "searched": searched})
    else:
        message = "since you haven't searched for any term"
        return render(request, 'pictures/filter.html', {"message": message})

