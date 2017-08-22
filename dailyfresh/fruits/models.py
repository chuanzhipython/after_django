from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=20)
    snum = models.IntegerField(11)

    def __str__(self):
        return self.sname