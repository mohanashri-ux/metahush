from typing import Any
from service.models import CatBreed,Category
from django.core.management.base import BaseCommand
import random

from django.templatetags.static import static
    
class Command(BaseCommand):
    help="This command inserts catbreed data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        CatBreed.objects.all().delete()
        
        
        names=[
           
            # cats
            "Persian Cat",
            "Siamese Cat",
            "Maine Coon",
            "Bengal Cat",
            "Ragdoll",
            "British Shorthair",
            "Sphynx",
            "Scottish Fold",
            "Abyssinian",
            "Norwegian Forest Cat",
            

            
]

        origins=[
          
            # cats
            "Originated in Iran (Persia), known for its long, luxurious fur and calm temperament.",
            "Native to Thailand, famous for its striking blue eyes and vocal personality.",
            "Developed in the state of Maine, USA, recognized as one of the largest domestic cat breeds.",
            "Bred in the USA and Asia by crossing domestic cats with Asian leopard cats to create a wild-looking breed.",
            "Originated in the United States, known for its docile and affectionate nature.",
            "Hails from the United Kingdom, famous for its dense coat and round face.",
            "Developed in Canada, known for its hairless appearance and friendly behavior.",
            "Originated in Scotland, easily recognized by its unique folded ears.",
            "Believed to have originated in Ethiopia, one of the oldest known cat breeds.",
            "Native to Norway, adapted to cold climates with its thick, water-resistant coat.",
]

        sizes=[
           
            # cats
            "1.5 ft",
            "1.5 ft",
            "3.5 ft",
            "2.5 ft", 
            "3 ft",
            "2 ft",
            "1.5 ft",
            "1.8 ft", 
            "2 ft",
            "3 ft",

]

        images=[
           
            # cats
            static("assets/img/cats_img/PersianCat.jpg"),
            static("assets/img/cats_img/SiameseCat.jpg"),
            static("assets/img/cats_img/MaineCoon.jpg"),
            static("assets/img/cats_img/BengalCat.jpg"),
            static("assets/img/cats_img/Ragdoll.jpg"),
            static("assets/img/cats_img/BritishShorthair.jpg"),
            static("assets/img/cats_img/Sphynx.jpg"),
            static("assets/img/cats_img/ScottishFold.jpg"),
            static("assets/img/cats_img/Abyssinian.jpg"),
            static("assets/img/cats_img/NorwegianForestCat.jpg"),
            
   

]

        categories=Category.objects.all()

        for name,origin,size,image in zip(names,origins,sizes,images):
            category=random.choice(categories)
            CatBreed.objects.create(name=name,origin=origin,size=size,image=image,category=category)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))