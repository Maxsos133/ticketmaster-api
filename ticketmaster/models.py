from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    bar = models.BooleanField()
    kitchen = models.BooleanField()
    bathrooms = models.IntegerField(null=True)
    outdoor_space = models.CharField(max_length=200, null=True)
    accessibility = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    performers = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    tickets_sold = models.IntegerField(null=True)
    tickets_available = models.IntegerField(null=True)

    def __str__(self):
        return self.name