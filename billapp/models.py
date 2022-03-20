from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField()
    description = models.TextField(blank=True)
    date_enrolled = models.DateField(auto_now_add=True)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
