from django.urls import path
from . import views


urlpatterns = [
    path("", views.bloghome, name="bloghome"),
    path("blogdetail/<int:blog_id>", views.blogdetail, name="blogdetail"),
    path("createnew/", views.createnew, name="createnew"),
    path("newpost/", views.newpost, name="newpost"),
]
