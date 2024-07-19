from django.shortcuts import render
from . models import Category,Content,animes,Movies
from django.db.models import Q

# Create your views here.


def home(req):
    Categorys = Category.objects.all()
    Contents = Content.objects.all()
    count = Category.objects.count()
    return render(req,'index.html',{'Category':Categorys, 'Content':Contents})



def anime(req):
    Categorys = Category.objects.all() 
    Category_name = Category.objects.get(name = 'Amine') 
    filt_cvideo = Content.objects.filter(category = Category_name)
    return render(req,'core/animes.html',{'Category':Categorys,'filt_cvideo':filt_cvideo})


def movies(req):
    Categorys = Category.objects.all()
    Category_name = Category.objects.get(name = 'Movies')
    filt_cvideo = Content.objects.filter(category = Category_name)
    return render(req,'core/movies.html',{'Category':Categorys,'filt_cvideo':filt_cvideo})


def category(req):
    Categorys = Category.objects.all()
    return render(req,'core/category/category.html',{'Category':Categorys})


def video(req,foo,pk):
    Categorys = Category.objects.all()
    Contents = Content.objects.get(id=pk)
    category_vid = Category.objects.get(name=foo)
    category_video_page = Content.objects.filter(category=category_vid)
    return render(req,'core/video.html',{'Category':Categorys,'Content':Contents,'category_video_page':category_video_page})



def category_one(req,foo):
    Categorys = Category.objects.all()
    category_name = Category.objects.get(name = foo)
    filt_video = Content.objects.filter(category = category_name)
    return render(req,'core/category/one_category.html',{'Category':Categorys ,'Fvideo':filt_video,'category_name':category_name})

def search(req):
    if req.POST:
        data = req.POST.get('search')
        Content_data = Content.objects.filter(title__icontains = data)
        Category_data = Category.objects.filter(name__icontains = data)
        return render(req,'search.html',{'Content_dataa': Content_data,'Category_data':Category_data} )
    return render(req,'search.html')


    


