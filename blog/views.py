from django.shortcuts import render

# Create your views here.
from .models import Post
def index(request):
    post = Post.objects.all()
    context = {
        'Judul':'MyBlog',
        'Heading':'Ini Adalah Blog',
        'Posts':post 
    }
    return render(request,'blog/index.html',context)

