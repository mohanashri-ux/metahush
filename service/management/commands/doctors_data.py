from typing import Any
from django.core.management.base import BaseCommand
from service.models import Doctor  # ✅ replace 'service' if needed
import random

class Command(BaseCommand):
    help = "Seed the database with sample doctor data"

    def handle(self, *args: Any, **options: Any):
        Doctor.objects.all().delete()

        names = [
            "Dr. Meera Iyer", "Dr. Rajeev Sharma", "Dr. Anjali Nair",
            "Dr. Karthik Reddy", "Dr. Shalini Verma", "Dr. Arjun Patel", "Dr. Sneha Ramesh"
        ]

        specializations = [
            "Veterinary Surgeon", "Animal Dermatologist", "Exotic Pet Specialist",
            "Veterinary Physician", "Avian Specialist", "Aquatic Animal Doctor", "General Practitioner"
        ]

        phones = [
            "9876543210", "9876543222", "9876543233",
            "9876543244", "9876543255", "9876543266", "9876543277"
        ]

        hospitals = [
            "Happy Paws Animal Clinic", "Care4Pets Hospital", "Exotic VetCare",
            "Green Valley Veterinary Center", "Bird & Beyond Care", "FishMed AquaCare", "PetCare Hospital"
        ]

        for name, spec, phone, hosp in zip(names, specializations, phones, hospitals):
            Doctor.objects.create(
                name=name,
                specialization=spec,
                phone=phone,
                hospital=hosp
            )

        self.stdout.write(self.style.SUCCESS("✅ Doctors inserted successfully."))
