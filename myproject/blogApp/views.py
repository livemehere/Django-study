from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.


def bloghome(request):
    posts = Blog.objects.all()
    return render(request, "bloghome.html", {"posts": posts})

    # path("blogdetail/<int:blog_id>", blogApp.views.bloghome, name="bloghome"),


def blogdetail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    print(post)
    return render(request, "blogdetail.html", {"post": post})


def createnew(request):
    if request.method == "POST":
        post = Blog()
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.write_date = timezone.localtime()
        post.modify_date = timezone.localtime()
        post.save()

        return redirect("/blogdetail/" + str(post.id))


def newpost(request):
    return render(request, "newpost.html")
