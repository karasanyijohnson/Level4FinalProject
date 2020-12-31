from django.db import models


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
    image = models.ImageField(upload_to='media/museums')
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{dict(self.MUSEUM_CATEGORIES)[self.category]}'


class Booking(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.firstName } has booked {self.museum} from {self.check_in} to {self.check_out}'
