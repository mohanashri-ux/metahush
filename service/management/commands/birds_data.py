from typing import Any
from service.models import BirdBreed,Category
from django.core.management.base import BaseCommand
import random


    
class Command(BaseCommand):
    help="This command inserts dogbreed data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        BirdBreed.objects.all().delete()
        
        
        names=[
            
            # birds
            "Parakeet (Budgerigar)",
            "Canary",
            "Cockatiel",
            "Lovebird",
            "African Grey Parrot",
            "Macaw",
            "Finch",
            "Cockatoo",
            "Quaker Parrot",
            "Amazon Parrot",
            
            

            
]

        origins=[
           
            # Birds
            "Native to Australia, known for their playful nature and ability to mimic speech.",
            "Originated from the Canary Islands, admired for their melodious singing abilities.",
            "Also from Australia, recognizable by their crest and affectionate behavior.",
            "Native to Africa and Madagascar, loved for their vibrant colors and strong bonding.",
            "From Central and West Africa, highly intelligent and capable of advanced speech mimicry.",
            "Found in Central and South America, notable for their large size and colorful feathers.",
            "Commonly found worldwide, known for their small size and cheerful chirping.",
            "Native to Australia and nearby islands, social and intelligent with expressive crests.",
            "Originates from South America, known for their lively personality and talking ability.",
            "Native to the Amazon Basin, vibrant and social birds with strong vocal skills.",
]

        sizes=[
            
            # birds
            "0.6 ft", 
            "0.5 ft",
            "0.8 ft",
            "0.5 ft",
            "1.3 ft", 
            "3.5 ft",
            "0.4 ft",
            "1.5 ft", 
            "1 ft", 
            "1.2 ft",

           
]

        images=[
           
            # birds
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/50/800/400",
            
   
]

        categories=Category.objects.all()

        for name,origin,size,image in zip(names,origins,sizes,images):
            category=random.choice(categories)
            BirdBreed.objects.create(name=name,origin=origin,size=size,image=image,category=category)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))