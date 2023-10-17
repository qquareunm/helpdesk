from django.db import models


# from datetime import date

# Create your models here.


class Problems(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    story = models.TextField(max_length=50000)

    CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(max_length=100, choices=CHOICES)

    STATUSES = [
        ('new', 'new'),
        ('resolved', 'resolved'),
    ]
    status = models.CharField(max_length=20, choices=STATUSES, default='new')

    date = models.DateField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     self.date = date.today()
    #     super(Problems, self).save(*args, **kwargs)