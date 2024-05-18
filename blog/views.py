from django.shortcuts import render, get_object_or_404
from .models import Tour, Service
# from .forms import 
 

def home(request):
    services=Service.objects.all()
    tours=Tour.objects.all()
    return render(request, 'home.html', context={"services":services, "tours":tours})

def tour(request, id):
    tour=get_object_or_404(Tour, id=id)
    services=tour.tour.all()
    tours=Tour.objects.all()
    return render(request, 'home.html', context={"services":services, "tour":tours})

def about(request):
    service=Service.objects.all()
    tour=Tour.objects.all()
    return render(request, 'about.html', context={"tour":tour} )

def view(request):
    servicess =Service.objects.all() 
    
    return render(request, 'view.html', context={"servicess": servicess})


