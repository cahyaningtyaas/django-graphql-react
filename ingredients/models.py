from django.db import models
# from model.utils import Choices
from django.contrib.postgres.fields import ArrayField
import datetime
from django.utils import timezone

# Create your models here.
STATUS = (
    ('0','waiting'),
    ('1', 'served')
)

class Chef (models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Customer (models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Dish (models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    duration = models.DurationField()
    # image = models.ImageField()
    def __str__(self):
        return  self.name

class DishOrder (models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    status = models.CharField(max_length=10)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    # ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    antrean = models.IntegerField(default=0)
    def __str__(self):
        return self.status

class Order (models.Model):
    # list = models.ForeignKey(DishOrder, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    waiting_time = models.DurationField()
    table = models.CharField(max_length=5)
    status = models.CharField(max_length=10,choices=STATUS) #, default=list) #models.CharField(max_length=10)
    created_at = models.DateTimeField()
    list = models.ManyToManyField(DishOrder)
    def __str__(self):
        return self.total
from django.db import models

# Create your models here.
