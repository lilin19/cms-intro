from django.shortcuts import render
from .models import Post
from django.template import loader

# Create your views here.
#:
#:def list_of_post(request):
#:  post = Post.objects.all()
#:  template = 'Dogfight/templates/post/list.html'
#:  context = {'post': post}
#:  return render(request, template, context)

def list_of_post(request):
    post = Post.objects.all()
    #: return the index.html
    content = {'post': post}

    template = './post/list.html'

    return render(request, template, content)

