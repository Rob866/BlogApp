from django.shortcuts import render
from .models import Post

posts = [
    {
        'autor' : 'Robert',
        'titulo': 'Blog Post 1',
        'contenido': 'Primer post content',
        'fecha_post': 'Agosto 27,2018'
    },
        {
        'autor' : 'Luis',
        'titulo': 'Blog Post 2',
        'contenido': 'Segundo post content',
        'fecha_post': 'Agosto 27,2018'
    }
]




def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)
    
def about(request):
    return render(request,'blog/about.html',{ 'titulo': 'About'})


