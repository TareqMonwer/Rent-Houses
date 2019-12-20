from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=255)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)
    contact_id = models.IntegerField(blank=True)
    realtor_email = models.EmailField()
    def __str__(self):
        return self.name
