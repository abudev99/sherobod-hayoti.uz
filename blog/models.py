from django.db import models

# Create your models here.
class Gazeta(models.Model):
    photo = models.FileField(upload_to='images/', blank=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Yangiliklar(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/', blank=True)
    body = models.TextField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.title