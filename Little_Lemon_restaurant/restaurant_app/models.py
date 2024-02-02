from django.db import models

# Create your models here.
class Menu(models.Model):
    Title=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=5,decimal_places=2)
    Image=models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.Title
class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    bookings_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name,self.date,self.time