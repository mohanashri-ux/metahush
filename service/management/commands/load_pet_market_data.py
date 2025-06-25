from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from service.models import PetMarket
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load sample pet market data (without duplicates)'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.WARNING('No users found. Creating a default user.'))
            user = User.objects.create_user(username='demo_user', password='password123')
        else:
            user = User.objects.first()

        listings = [
            {
                "listing_type": "Sell",
                "pet_type": "Dog",
                "breed": "Golden Retriever",
                "age": 2.5,
                "price": 15000.00,
                "description": "Friendly and playful Golden Retriever, vaccinated and healthy.",
                "contact_number": "9876543210",
                "city": "Chennai",
                "image": "pet_market/golden_retriever.jpg"
            },
            {
                "listing_type": "Sell",
                "pet_type": "Cat",
                "breed": "Persian",
                "age": 1.2,
                "price": 9000.00,
                "description": "Cute white Persian cat, loves cuddles and calm environment.",
                "contact_number": "9345612780",
                "city": "Bangalore",
                "image": "pet_market/persian.jpg"
            },
            {
                "listing_type": "Sell",
                "pet_type": "Bird",
                "breed": "Parrot",
                "age": 0.8,
                "price": 2000.00,
                "description": "Looking to buy a talking parrot, preferably trained.",
                "contact_number": "9988776655",
                "city": "Hyderabad",
                "image": "pet_market/macaw.jpg"
            },
            {
                "listing_type": "Sell",
                "pet_type": "Fish",
                "breed": "Goldfish",
                "age": 0.5,
                "price": 500.00,
                "description": "Healthy goldfish pair with tank accessories.",
                "contact_number": "9123456789",
                "city": "Delhi",
                "image": "pet_market/goldfish.jpg"
            },
            {
                "listing_type": "Sell",
                "pet_type": "Dog",
                "breed": "Beagle",
                "age": 3.0,
                "price": 12000.00,
                "description": "Energetic beagle, great with kids. Fully vaccinated.",
                "contact_number": "9876501234",
                "city": "Mumbai",
                "image": "pet_market/beagle.jpg"
            }
        ]

        for item in listings:
            PetMarket.objects.get_or_create(
                user=user,
                listing_type=item["listing_type"],
                pet_type=item["pet_type"],
                breed=item["breed"],
                city=item["city"],
                defaults={
                    "age": Decimal(str(item["age"])),
                    "price": Decimal(str(item["price"])),
                    "description": item["description"],
                    "contact_number": item["contact_number"],
                    "image": item["image"],
                    "available": True
                }
            )

        self.stdout.write(self.style.SUCCESS("Sample pet market data loaded successfully."))
