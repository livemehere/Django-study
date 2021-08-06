from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def bloghome(request):
    posts = Blog.objects.all()
    return render(request, "bloghome.html", {"posts": posts})

    # path("blogdetail/<int:blog_id>", blogApp.views.bloghome, name="bloghome"),


def blogdetail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    print(post)
    return render(request, "blogdetail.html", {"post": post})
