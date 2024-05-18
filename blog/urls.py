from django.urls import path
from .views import home, tour, about, view


urlpatterns = [
   path('home', home, name="home"),
   path('tour/<int:id>/', tour, name="tour"),
   path('about', about, name="about"),
   path('view/', view, name="view"),
   
   
   

    
]
