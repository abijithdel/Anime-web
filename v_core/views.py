from django.shortcuts import render
from . models import Category,Content,animes,Movies
from django.db.models import Q

# Create your views here.


def home(req):
    Categorys = Category.objects.all()
    Contents = Content.objects.all()
    return render(req,'index.html',{'Category':Categorys, 'Content':Contents})



def anime(req):
    Categorys = Category.objects.all() 
    ani = animes.objects.all()
    return render(req,'core/animes.html',{'Category':Categorys,'animes':ani})


def movies(req):
    Categorys = Category.objects.all()
    mvi = Movies.objects.all()
    return render(req,'core/movies.html',{'Category':Categorys,'Movies':mvi})


def category(req):
    Categorys = Category.objects.all()
    return render(req,'core/category/category.html',{'Category':Categorys})


def video(req,pk):
    Categorys = Category.objects.all()
    Contents = Content.objects.get(id=pk)
    return render(req,'core/video.html',{'Category':Categorys,'Content':Contents})

def anime_video(req,pk):
    Categorys = Category.objects.all()
    mvi_vie = animes.objects.get(id=pk)
    return render(req,'core/anime_video.html',{'Category':Categorys,'Content':mvi_vie})

def movies_video(req,pk):
    Categorys = Category.objects.all()
    ani_vie = Movies.objects.get(id=pk)
    return render(req,'core/movies_video.html',{'Category':Categorys,'Content':ani_vie})

def category_one(req,foo):
    Categorys = Category.objects.all()
    category_name = Category.objects.get(name = foo)
    filt_video = Content.objects.filter(category = category_name)
    return render(req,'core/category/one_category.html',{'Category':Categorys ,'Fvideo':filt_video,'category_name':category_name})

def search(req):
    search_data = []
    if req.POST:
        data = req.POST.get('search')
        Content_data = Content.objects.filter(title__icontains = data)
        animes_data = animes.objects.filter(atitle__icontains = data)
        Movies_data = Movies.objects.filter(mtitle__icontains = data)

        return render(req,'search.html',{'Content_dataa': Content_data,'animes_data':animes_data,'Movies_data':Movies_data} )
    return render(req,'search.html')


    


