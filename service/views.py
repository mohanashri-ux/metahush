from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
from .forms import UserRegistrationForm
from .models import DogBreed, CatBreed, FishBreed,BirdBreed,OtherBreed
from django.http import Http404
from django.core.paginator import Paginator
from .models import GroomingProduct
from .models import PetMarket
from .models import PetSittingService
from .forms import PetSittingServiceForm
from datetime import timedelta
from .forms import PetInsuranceForm
from .forms import FeedbackForm


from .models import Appointment, Doctor
from django.db.models import Count
import random



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



def appointment_form(request):
    return render(request, 'appointment.html')

def submit_appointment(request):
    if request.method == 'POST':
        appointment = Appointment.objects.create(
            owner_name=request.POST['owner_name'],
            pet_name=request.POST['pet_name'],
            species=request.POST['species'],
            breed=request.POST['breed'],
            problem=request.POST['problem'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            date=request.POST['date'],
            time=request.POST['time']
        )
        random_doctor = Doctor.objects.order_by('?').first() # random doctor
        return render(request, 'doctor.html', {
            'doctor': random_doctor,
            'appointment_id': appointment.id
        })
    return redirect('appointment_form')

def confirm_appointment(request):
    if request.method == 'POST':
        # You can update the appointment record to assign doctor here
        # Example:
        appointment_id = request.POST['appointment_id']
        doctor_id = request.POST['doctor_id']
        # Save assignment (optional)
        Appointment.objects.filter(id=appointment_id).update(doctor_id=doctor_id)
        return redirect('index')  # or render with success message


def grooming_products(request):
    products=GroomingProduct.objects.all()
    # You can fetch product data from database if available
    return render(request, 'grooming_products.html',{'products':products})


def pet_market_list(request):
    print("check")
    pets = PetMarket.objects.filter(available=True).order_by('-created_at')
    return render(request, 'pet_market_list.html', {'pets': pets})

def calculate_cost(sitting_type,days):
    if sitting_type=='home':
        return days * 500
    elif sitting_type=='care':
        return days*800
    return 0

def book_pet_sitting(request):
    if request.method == 'POST':
        form = PetSittingServiceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            days = (instance.to_date - instance.from_date).days + 1
            instance.cost = calculate_cost(instance.sitting_type, days)
            instance.save()
            return render(request, 'confirm_booking.html', {'booking': instance})
    else:
        form = PetSittingServiceForm()

    return render(request, 'pet_sitting_form.html', {'form': form})

def payment_page(request):
    booking_id = request.GET.get('booking_id')
    booking = get_object_or_404(PetSittingService, id=booking_id)

    if request.method == 'POST':
        method = request.POST.get('payment_method')
        # You could save this info to DB, redirect, or mock confirmation
        return render(request, 'payment_successful.html', {'booking': booking, 'method': method})

    return render(request, 'payment_page.html', {'booking': booking})


def insurance_plans_page(request):
    return render(request, 'insurance_plans.html')


def pet_insurance_view(request):
    if request.method == 'POST':
        form = PetInsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'insurance_success.html')
    else:
        form = PetInsuranceForm()
    return render(request, 'pet_insurance.html', {'form': form})



def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
