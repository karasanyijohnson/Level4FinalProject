from django.db import models
from django.contrib.auth.models import User


class Museum(models.Model):
    MUSEUM_CATEGORIES = (

        ("CAMPAIGN AGAINST GENOCIDE", "CAMPAIGN AGAINST GENOCIDE"),
        ("RWANDA ART", "RWANDA ART"),
        ("KING'S PALACE", "KING'S PALACE"),
        ("NATIONAL LIBERATION", "NATIONAL LIBERATION"),
        ("ENVIRONMENT", "ENVIRONMENT"),
        ("NATIONAL ART GALLERY", "NATIONAL ART GALLERY"),
        ("KANDT'S HOUSE", "KANDT'S HOUSE"),
        ("ETHNOGRAPHIC", "ETHNOGRAPHIC")

    )
    category = models.CharField(max_length=50, choices=MUSEUM_CATEGORIES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/museums')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Booking(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return self.firstName