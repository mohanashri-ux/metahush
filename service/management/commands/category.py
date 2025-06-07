from typing import Any
from service.models import Category
from django.core.management.base import BaseCommand



    
class Command(BaseCommand):
    help="This command inserts category data"
    
    def handle(self, *args:Any, **options:Any):
        
        #Deleting existing data
        Category.objects.all().delete()
        
        
        categories=['Dogs','Cats','Pisces','others','Special breeds']
        
   
        for category_name in categories:
            Category.objects.create(name=category_name)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))