from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def movie_detail(request):
    return render(request,'movie_detail.html')
