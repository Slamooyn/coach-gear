from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):

    CATEGORY_CHOICES = [
    ('futsal', 'Futsal'),
    ('sepakbola', 'Sepak Bola'),
    ('badminton', 'Badminton'),
    ('basket', 'Basket'),
    ('voli', 'Voli'),
    ('tenis', 'Tenis'),
    ('other','Other')
]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='-')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    

    



