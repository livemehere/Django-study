from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import helloworld.views
import wordcount.views
import blogApp.views
import staticfile.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", helloworld.views.helloworld, name="home"),
    path("wordcount/", wordcount.views.wordcount, name="wordcount"),
    path("result/", wordcount.views.result, name="result"),
    path("blog/", include("blogApp.urls")),
    path("staticfile/", staticfile.views.staticfile, name="staticfile"),
]
