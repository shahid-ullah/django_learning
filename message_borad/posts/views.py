from django.shortcuts import render
from .models import Post

def home(request):

    post_list = Post.objects.all()

    return render(request, 'home.html', context={'post_list': post_list})

