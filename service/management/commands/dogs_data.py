from typing import Any
from service.models import DogBreed,Category
from django.core.management.base import BaseCommand
import random


    
class Command(BaseCommand):
    help="This command inserts dogbreed data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        DogBreed.objects.all().delete()
        
        
        names=[
            # dogs
            "Labrador Retriever",
            "German Shepherd",
            "Golden Retriever",
            "Bulldog",
            "Poodle",
            "Beagle",
            "Rottweiler",
            "Dachshund",
            "Siberian Husky",
            "Shih Tzu",
            
            
]

        origins=[
            # dogs
            "Developed in Newfoundland for retrieving fishing nets and assisting hunters.",
            "Bred in the late 1800s for herding and protecting sheep; later used in police and military.",
            "Bred in the 19th century for retrieving game from water and land during hunting.",
            "Originated in the 13th century for bull-baiting; later became a companion breed.",
            "Originally bred as a water retriever; popular in France as a companion dog.",
            "Developed as a scent hound for hunting hare and rabbits.",
            "Descended from Roman drover dogs used to herd cattle and pull carts.",
            "Bred to hunt badgers and burrow-dwelling animals; name means 'badger dog' in German.",
            "Developed by the Chukchi people for sled-pulling and companionship.",
            "Bred as companion dogs for Chinese royalty; name means 'lion dog' in Mandarin.",
]

        sizes=[
            # dogs
            "4ft",
            "2ft",
            "6ft",
            "5ft",
            "4ft",
            "3ft",
            "2ft",
            "6ft",
            "3ft",
            "5ft",
           

]

        images=[
            # dogs
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
            "https://picsum.photos/id/237/800/400",
          
    # {
    #     "image": ["https://images.dog.ceo/breeds/retriever-golden/n02099601_100.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/germanshepherd/n02106662_1234.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/retriever-labrador/n02099712_3929.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/bulldog-english/jager-1.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/poodle-toy/n02113624_955.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/beagle/n02088364_11136.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/rottweiler/n02106550_6502.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/dachshund/dog-1210559_640.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/husky/n02110185_1469.jpg"]
    # },
    # {
    #     "image": ["https://images.dog.ceo/breeds/pekinese/n02086079_445.jpg"]
    # }
]

        categories=Category.objects.all()

        for name,origin,size,image in zip(names,origins,sizes,images):
            category=random.choice(categories)
            DogBreed.objects.create(name=name,origin=origin,size=size,image=image,category=category)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))