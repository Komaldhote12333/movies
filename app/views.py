from django.shortcuts import render
from .models import*
from django.shortcuts import redirect

# Create your views herdef
def index(request):
    category = Category.objects.all().order_by("-id")
    
    categoryfrontthree = Category.objects.all().order_by("-id")[:3]
    
    Serchname = request.GET.get('serchname')
    
    categoryid = request.GET.get('Categoryid')
    if categoryid:
        movie = Movie.objects.filter(movitype=categoryid).order_by("-id")
  
       
        
            
            
          
        
        
    else:
        movie = Movie.objects.all().order_by("-id")[:20]
  
    data = {
        
        'category':category,
        'movie':movie,
        'categoryfrontthree':categoryfrontthree,
    }
  
    return render(request,"index.html",data)


def total(request):
    return redirect("index")


def searchmov(request):    
    Serchname = request.GET.get('serchname')
    movie = Movie.objects.filter(name__icontains =Serchname).order_by("-id")
    
    if movie:
        
       
        data = {
        
        
        'movie':movie,
     
         }
  
        return render(request,"new.html",data)
    
    return render(request,"new.html")
       
        
            
            
          
        
      
    data = {
        
        
        'movie':movie,
     
    }
  
    return redirect("index")


def team(request):
    members= Team.objects.all().order_by("-id")
    return render(request,'team.html',{'members':members})
 