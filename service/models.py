from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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

# from django.db import models
# from django.utils.text import slugify
# from .models import Category  # adjust import if Category is in another app

class CatBreed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    image = models.ImageField(upload_to='cat_breeds/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='cat_breeds',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class FishBreed(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='fish_breeds/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fish_breeds', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class OtherBreed(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='other_breeds/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='other_breeds', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BirdBreed(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='bird_breeds/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bird_breeds', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    ]

    owner_name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    problem = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.pet_name} - {self.owner_name}"

class GroomingProduct(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='grooming_products/',blank=True,null=True)
    
    def __str__(self):
        return self.name
    


class PetMarket(models.Model):
    SELL = 'Sell'
    BUY = 'Buy'

    LISTING_TYPE_CHOICES = [
        (SELL, 'Sell'),
        (BUY, 'Buy'),
    ]

    PET_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Fish', 'Fish'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_market_listings')
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES, default=SELL)
    pet_type = models.CharField(max_length=20, choices=PET_CHOICES)
    breed = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=4, decimal_places=1, help_text="Age in years (e.g., 1.5)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Selling price or offer")
    description = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_market/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.listing_type} - {self.pet_type} ({self.breed}) by {self.user.username}"
