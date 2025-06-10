from django.db import models
from django.utils.text import slugify

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
    
    
#category
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    image = models.ImageField(upload_to='dog_breeds/', blank=True, null=True)
    slug=models.SlugField(unique=True) #to make sure every slug field's values are unique
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='breeds', null=True, blank=True)

    
    # to save those slugs
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name) #generate url based on name category of that species to avoid hackers to know how many species we have in db
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    


class LoginData(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)  # Store hashed password ideally
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

