from django.db import models


class Comment(models.Model): 
    date = models.DateField()
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)