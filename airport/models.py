from django.conf import settings
from django.db import models


class Crew(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class AirplaneType(models.Model):
    name = models.CharField(max_length=50)


class Airplane(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)


class Airport(models.Model):
    name = models.CharField(max_length=50)
    closest_big_city = models.CharField(max_length=50)


class Route(models.Model):
    source = models.ManyToManyField(Airport, blank=True)
    destination = models.ManyToManyField(Airport, blank=True)
    distance = models.IntegerField(default=0)


class Flight(models.Model):
    route = models.ManyToManyField(Route, blank=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
