from django.shortcuts import render

# Create your views here.


def staticfile(req):
    return render(req, "staticfile.html")
