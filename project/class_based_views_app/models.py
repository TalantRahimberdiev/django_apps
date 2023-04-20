from django.db import models

# Create your models here.

class Studies(models.Model):
    subject=models.CharField(max_length=33)
    description=models.TextField()
    start_date=models.DateField()

    def __str__(self):
        return self.subject

