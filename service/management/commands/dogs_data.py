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
            
            # pisces
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
            
            # others
            "Small mammals",
            "Reptiles",
            "Amphibians",
            "Giant mammals",
            "Exotic birds",

            
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
            # pisces
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
            # others
            "Found in various parts of the world, small mammals like hamsters, guinea pigs, and rabbits have been domesticated for companionship due to their gentle nature and manageable size.",
            "Originating from warm and tropical regions globally, reptiles such as lizards, turtles, and snakes have adapted to diverse habitats, making them popular as low-maintenance exotic pets.",
            "Native to moist and aquatic environments across continents, amphibians like frogs, toads, and salamanders are known for their dual life stages and sensitivity to environmental changes.",
            "Typically found in forests, savannas, and mountainous regions, giant mammals such as elephants, giraffes, and bison are admired for their majestic size but are rarely kept outside of wildlife reserves.",
            "Originating from tropical rainforests, exotic birds like macaws, toucans, and cockatoos are cherished for their vivid plumage and intelligence, often requiring specialized care in captivity.",
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

            # pisces
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

            # others
            "1 to 2 ft", 
            "1 to 6 ft", 
            "0.2 to 1 ft", 
            "6 to 13 ft",
            "1 to 3 ft",

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
            
            # cats
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/40/800/400",
            # pisces
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
            "https://picsum.photos/id/218/800/400",
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
            # others
            "https://picsum.photos/id/244/800/400",
            "https://picsum.photos/id/258/800/400",
            "https://picsum.photos/id/275/800/400",
            "https://picsum.photos/id/433/800/400",
            "https://picsum.photos/id/477/800/400",
   
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