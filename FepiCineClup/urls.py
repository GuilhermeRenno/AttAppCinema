
from django.urls import path
from FepiCineClup.views import home, movie_detail

urlpatterns = [
    path('home/', home),
    path('detail/',movie_detail)
    
]