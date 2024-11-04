from django.shortcuts import render
# from .views import index
# Create your views here.


def index(request):
    return render(request, 'links/index.html', {})
