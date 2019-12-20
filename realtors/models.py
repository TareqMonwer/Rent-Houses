from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'realtors'

    def __str__(self):
        return self.name
