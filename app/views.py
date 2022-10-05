from django.shortcuts import render
from .models import Post
# Create your views here.
def posts(request):
    all = Post.objects.all()
    context = {
        "posts":all
    }
    return render(request,'index.html',context)
