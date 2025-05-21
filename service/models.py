from django.db import models

# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    
    
class UserRegistration(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20, choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    image = models.ImageField(upload_to='dog_breeds/', blank=True, null=True)

    def __str__(self):
        return self.name