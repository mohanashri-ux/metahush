from typing import Any
from django.core.management.base import BaseCommand
from service.models import Category, DogBreed, CatBreed, FishBreed, OtherBreed, BirdBreed
from django.utils.text import slugify


class Command(BaseCommand):
    help = "This command inserts breed data for all categories"

    def handle(self, *args: Any, **options: Any):
        # Clear existing data
        DogBreed.objects.all().delete()
        CatBreed.objects.all().delete()
        FishBreed.objects.all().delete()
        OtherBreed.objects.all().delete()
        BirdBreed.objects.all().delete()

        breeds_data = [
            {
                'model': DogBreed,
                'category': 'Dogs',
                'items': [
                    {"name": "Labrador", "origin": "Canada", "size": "large", "image": "dog.jpg"},
                    {"name": "Beagle", "origin": "England", "size": "medium", "image": "dog.jpg"},
                ]
            },
            {
                'model': CatBreed,
                'category': 'Cats',
                'items': [
                    {"name": "Persian Cat", "origin": "Iran", "size": "medium", "image": "cat.jpg"},
                    {"name": "Siamese", "origin": "Thailand", "size": "small", "image": "cat.jpg"},
                ]
            },
            {
                'model': FishBreed,
                'category': 'Pisces',
                'items': [
                    {"name": "Goldfish", "origin": "China", "size": "small", "image": "fish.jpg"},
                    {"name": "Betta", "origin": "Thailand", "size": "small", "image": "fish.jpg"},
                ]
            },
            {
                'model': OtherBreed,
                'category': 'Others',
                'items': [
                    {"name": "Hamster", "origin": "Worldwide", "size": "small", "image": "other.jpg"},
                    {"name": "Iguana", "origin": "Mexico", "size": "medium", "image": "other.jpg"},
                ]
            },
            {
                'model': BirdBreed,
                'category': 'Birds',
                'items': [
                    {"name": "Macaw", "origin": "South America", "size": "large", "image": "bird.jpg"},
                    {"name": "Cockatiel", "origin": "Australia", "size": "medium", "image": "bird.jpg"},
                ]
            }
        ]

        for group in breeds_data:
            model = group['model']
            category_name = group['category']
            category = Category.objects.get(name=category_name)
            for item in group['items']:
                model.objects.create(
                    name=item['name'],
                    origin=item['origin'],
                    size=item['size'],
                    image=item['image'],
                    slug=slugify(item['name']),
                    category=category
                )

        self.stdout.write(self.style.SUCCESS("All breed data inserted."))
