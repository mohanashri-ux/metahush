from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
from .forms import UserRegistrationForm
from .models import DogBreed, CatBreed, FishBreed,BirdBreed,OtherBreed
from django.http import Http404
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    features=Feature.objects.all()  
    return render(request,'index.html',{'features':features})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists!')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('index')
        else:
            messages.info(request,'Passwords does not match')
            return redirect('register')
    else:
        return render(request,'register.html')
    
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import LoginData

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Save the login data
            LoginData.objects.create(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']  # For real app, hash the password
            )
            return render(request, 'index.html')  # or redirect to dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

    
def logout(request):
    auth.logout(request)
    return redirect('/')

def dog_breed_list(request):
    # getting data from dogbreed model
    breeds = DogBreed.objects.all()
    # print("All breeds from DB:", breeds)
    return render(request, 'dog_breed_list.html', {'breeds': breeds})

# def detail(request,slug):
#     try:
#         breed=DogBreed.objects.get(slug=slug)
#         related_breeds=DogBreed.objects.filter(category=breed.category).exclude(pk=breed.id)
        
#     except DogBreed.DoesNotExist:
#         raise Http404("Breed doesn't exist!")
        


# Mapping species type to model
BREED_MODEL_MAP = {
    'dog': DogBreed,
    'cat': CatBreed,
    'fish': FishBreed,
    'bird': BirdBreed,
    'other': OtherBreed,
}

def detail(request, species, slug):
    model = BREED_MODEL_MAP.get(species.lower())
    if not model:
        raise Http404("Species not found!")

    # Fetch the breed object
    breed = get_object_or_404(model, slug=slug)

    # Related breeds of same category
    related_breeds = model.objects.filter(category=breed.category).exclude(pk=breed.pk)

    return render(request, 'details.html', {
        'breed': breed,
        'related_breeds': related_breeds,
        'species': species,
    })

# def detail(request,slug):
#     try:
#         breed=DogBreed.objects.get(slug=slug)
#         related_breeds=DogBreed.objects.filter(category=breed.category).exclude(pk=breed.id)
        
#     except DogBreed.DoesNotExist:
#         raise Http404("Breed doesn't exist!")
        
        
        
#     return render(request,'details.html',{'breed':breed,'related_breeds':related_breeds})

# def payment_view(request):
#     if request.method == 'POST':
#         dog_id = request.POST.get('dog_id')
#         return render(request, 'eStore/payment.html', {'dog_id': dog_id})

def cat_breed_list(request):
    # getting data from dogbreed model
    breeds = CatBreed.objects.all()
    # print("All breeds from DB:", breeds)
    return render(request, 'cat_breed_list.html', {'breeds': breeds})

def fish_breed_list(request):
    breeds = FishBreed.objects.all()
    return render(request, 'fish_breed_list.html', {'breeds': breeds})

def bird_breed_list(request):
    breeds = BirdBreed.objects.all()
    return render(request, 'bird_breed_list.html', {'breeds': breeds})


def other_breed_list(request):
    breeds = OtherBreed.objects.all()
    return render(request, 'other_breed_list.html', {'breeds': breeds})