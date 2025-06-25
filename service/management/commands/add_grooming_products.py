from django.core.management.base import BaseCommand
from service.models import GroomingProduct

class Command(BaseCommand):
    help = 'Add 30 sample grooming products'

    def handle(self, *args, **kwargs):
        products = [
            {"name": "Pet Shampoo", "description": "Gentle cleansing for dogs and cats.", "price": 299.00, "image": "grooming_products/shampoo.jpg"},
            {"name": "Pet Brush", "description": "Removes tangles and loose fur effectively.", "price": 199.00, "image": "grooming_products/brush.jpg"},
            {"name": "Nail Clipper", "description": "Safe nail clipper for all pet sizes.", "price": 149.00, "image": "grooming_products/clipper.jpg"},
            {"name": "Pet Towel", "description": "Highly absorbent towel for drying pets after bath.", "price": 249.00, "image": "grooming_products/towel.jpg"},
            {"name": "Ear Cleaner", "description": "Soothing ear cleaner for preventing infections.", "price": 179.00, "image": "grooming_products/ear_cleaner.jpg"},
            {"name": "Dental Chew Sticks", "description": "Cleans teeth and freshens breath.", "price": 129.00, "image": "grooming_products/chew_sticks.jpg"},
            {"name": "Pet Cologne", "description": "Keeps your pet smelling fresh and clean.", "price": 199.00, "image": "grooming_products/cologne.jpg"},
            {"name": "Flea Comb", "description": "Removes fleas, eggs, and dirt from fur.", "price": 99.00, "image": "grooming_products/flea_comb.jpg"},
            {"name": "Grooming Scissors", "description": "Precision trimming with rounded safety tips.", "price": 249.00, "image": "grooming_products/scissors.jpg"},
            {"name": "De-shedding Tool", "description": "Reduces shedding up to 90%.", "price": 349.00, "image": "grooming_products/deshedding_tool.jpg"},
            {"name": "Pet Wipes", "description": "Alcohol-free wipes for daily cleaning.", "price": 199.00, "image": "grooming_products/wipes.jpg"},
            {"name": "Undercoat Rake", "description": "Helps remove thick undercoats in dogs.", "price": 299.00, "image": "grooming_products/undercoat_rake.jpg"},
            {"name": "Paw Balm", "description": "Soothes and heals dry or cracked paws.", "price": 149.00, "image": "grooming_products/paw_balm.jpg"},
            {"name": "Tick Remover Tool", "description": "Easy and safe removal of ticks.", "price": 89.00, "image": "grooming_products/tick_remover.jpg"},
            {"name": "Slicker Brush", "description": "Ideal for long-haired breeds.", "price": 199.00, "image": "grooming_products/slicker_brush.jpg"},
            {"name": "Pet Dryer", "description": "Quick drying after baths.", "price": 999.00, "image": "grooming_products/pet_dryer.jpg"},
            {"name": "Pet Grooming Kit", "description": "Complete tools for home grooming.", "price": 1299.00, "image": "grooming_products/grooming_kit.jpg"},
            {"name": "Eye Wipes", "description": "Removes tear stains safely.", "price": 159.00, "image": "grooming_products/eye_wipes.jpg"},
            {"name": "Pet Bath Gloves", "description": "Massaging gloves for bathing and grooming.", "price": 229.00, "image": "grooming_products/bath_gloves.jpg"},
            {"name": "Coat Shine Spray", "description": "Adds shine and reduces tangles.", "price": 179.00, "image": "grooming_products/shine_spray.jpg"},
            {"name": "Pet Hair Remover Roller", "description": "Quickly removes pet hair from fabric.", "price": 149.00, "image": "grooming_products/hair_remover.jpg"},
            {"name": "Pet Grooming Apron", "description": "Waterproof and hair-proof apron.", "price": 299.00, "image": "grooming_products/apron.jpg"},
            {"name": "Pet Perfume", "description": "Long-lasting fragrance for pets.", "price": 249.00, "image": "grooming_products/perfume.jpg"},
            {"name": "Tearless Puppy Shampoo", "description": "Mild shampoo for puppies.", "price": 269.00, "image": "grooming_products/puppy_shampoo.jpg"},
            {"name": "Silicone Pet Scrubber", "description": "Deep cleansing brush for fur.", "price": 199.00, "image": "grooming_products/scrubber.jpg"},
            {"name": "Pet Grooming Table", "description": "Portable table for easy grooming.", "price": 2499.00, "image": "grooming_products/grooming_table.jpg"},
            {"name": "Deodorizing Spray", "description": "Neutralizes bad odors instantly.", "price": 179.00, "image": "grooming_products/deodorizer.jpg"},
            {"name": "Whitening Shampoo", "description": "Brightens white and light-colored coats.", "price": 299.00, "image": "grooming_products/whitening_shampoo.jpg"},
            {"name": "Ear Powder", "description": "Keeps ears dry and clean.", "price": 139.00, "image": "grooming_products/ear_powder.jpg"},
            {"name": "Double-Sided Comb", "description": "Wide and fine tooth combo for detangling.", "price": 159.00, "image": "grooming_products/comb.jpg"}
        ]

        for item in products:
            GroomingProduct.objects.get_or_create(
                name=item['name'],
                defaults={
                    'description': item['description'],
                    'price': item['price'],
                    'image': item['image'],
                }
            )

        self.stdout.write(self.style.SUCCESS("30 Grooming products added successfully."))
