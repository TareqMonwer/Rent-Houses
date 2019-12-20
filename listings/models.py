from django.db import models
from datetime import datetime

from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqr_ft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
    photo1 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'listings'

    def __str__(self):
        return self.title
