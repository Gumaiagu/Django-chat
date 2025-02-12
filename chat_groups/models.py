from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Mensage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField("date published")

    def __str__(self):
        return self.content
