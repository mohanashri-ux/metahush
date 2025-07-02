from typing import Any
from service.models import FishBreed,Category
from django.core.management.base import BaseCommand
import random
from django.templatetags.static import static

    
class Command(BaseCommand):
    help="This command inserts dogbreed data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        FishBreed.objects.all().delete()
        
        
        names=[
           
            
            # fishes
            "Goldfish",
            "Betta",
            "Guppy",
            "Koi",
            "Angelfish",
            "Neon Tetra",
            "Discus",
            "Clownfish",
            "Molly",
            "Swordtail",
            
            
]

        origins=[
           
            # fishes
            "Bred in ancient China, commonly kept as ornamental fish in freshwater tanks.",
            "Native to Thailand, known for vibrant colors and territorial behavior.",
            "Found in South America, popular for bright patterns and easy breeding.",
            "Developed in Japan, symbolizes luck and prosperity in Japanese culture.",
            "Native to the Amazon River, admired for graceful fins and triangular body.",
            "Originates from South America, known for its neon blue and red stripes.",
            "Native to the Amazon Basin, recognized for its round shape and vivid colors.",
            "Found in the warm waters of the Pacific and Indian Oceans, famous for its clown-like appearance.",
            "Originally from Central and South America, valued for peaceful nature and easy care.",
            "Native to North and Central America, easily recognized by its sword-shaped tail.",
]

        sizes=[
           
            # fishes
            "0.5 ft",
            "0.3 ft",
            "0.2 ft",
            "2 ft", 
            "0.6 ft",
            "0.1 ft",
            "0.8 ft",
            "0.4 ft",
            "0.3 ft",
            "0.4 ft",
            
]

        images=[
            
            # fishes
            static("assets/img/fishes_img/Goldfish.jpg"),
            static("assets/img/fishes_img/Betta.jpg"),
            static("assets/img/fishes_img/Guppy.jpg"),
            static("assets/img/fishes_img/Koi.jpg"),
            static("assets/img/fishes_img/Angelfish.jpg"),
            static("assets/img/fishes_img/NeonTetra.jpg"),
            static("assets/img/fishes_img/Discus.jpg"),
            static("assets/img/fishes_img/Clownfish.jpg"),
            static("assets/img/fishes_img/Molly.jpg"),
            static("assets/img/fishes_img/Swordtail.jpg"),
            
]

        categories=Category.objects.all()

        for name,origin,size,image in zip(names,origins,sizes,images):
            category=random.choice(categories)
            FishBreed.objects.create(name=name,origin=origin,size=size,image=image,category=category)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))