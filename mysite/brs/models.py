from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bus(models.Model):
    STATUS_CHOICES = (('available', 'Available'), ('not_available', 'Not Available'),)
    title = models.CharField(max_length=250)
    number = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    departure_time = models.DateTimeField()
    destination = models.CharField(max_length=250)
    available_seats = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    class Meta:
        ordering = ('-available_seats',)
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
    def __str__(self):
        return self.title + " - " + self.number

class Ticket(models.Model):
    name = models.CharField(max_length=250)
    number = models.PositiveIntegerField(unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    bus = models.ForeignKey(Bus,
                            on_delete=models.CASCADE,
                            related_name='tickets')
    booked_seats = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)
