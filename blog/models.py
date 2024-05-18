from django.db import models

# Create your models here.

class Tour(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"
    
    
class Service(models.Model):
    country=models.CharField(max_length=200)
    destination=models.IntegerField()
    tour=models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="tour")
    image=models.ImageField(upload_to='service_image/', null=True)
        
    def __str__(self):
        return f"{self.country}"
