from typing import Any
from service.models import OtherBreed,Category
from django.core.management.base import BaseCommand
import random
from django.templatetags.static import static

    
class Command(BaseCommand):
    help="This command inserts dogbreed data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        OtherBreed.objects.all().delete()
        
        
        names=[
            
            # others
            "Small mammals",
            "Reptiles",
            "Amphibians",
            "Giant mammals",
            "Exotic birds",

            
]

        origins=[
            
            # others
            "Found in various parts of the world, small mammals like hamsters, guinea pigs, and rabbits have been domesticated for companionship due to their gentle nature and manageable size.",
            "Originating from warm and tropical regions globally, reptiles such as lizards, turtles, and snakes have adapted to diverse habitats, making them popular as low-maintenance exotic pets.",
            "Native to moist and aquatic environments across continents, amphibians like frogs, toads, and salamanders are known for their dual life stages and sensitivity to environmental changes.",
            "Typically found in forests, savannas, and mountainous regions, giant mammals such as elephants, giraffes, and bison are admired for their majestic size but are rarely kept outside of wildlife reserves.",
            "Originating from tropical rainforests, exotic birds like macaws, toucans, and cockatoos are cherished for their vivid plumage and intelligence, often requiring specialized care in captivity.",
]

        sizes=[
            

            # others
            "1 to 2 ft", 
            "1 to 6 ft", 
            "0.2 to 1 ft", 
            "6 to 13 ft",
            "1 to 3 ft",

]

        images=[
            
            # others
            static("assets/img/others_img/Smallmammals.jpg"),
            static("assets/img/others_img/Reptiles.jpg"),
            static("assets/img/others_img/Amphibians.jpg"),
            static("assets/img/others_img/Giantmammals.jpg"),
            static("assets/img/others_img/Exoticbirds.jpg"),
            
]

        categories=Category.objects.all()

        for name,origin,size,image in zip(names,origins,sizes,images):
            category=random.choice(categories)
            OtherBreed.objects.create(name=name,origin=origin,size=size,image=image,category=category)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))