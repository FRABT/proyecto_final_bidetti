from django.db import models


class Blog(models.Model):
    date = models.DateField()
    autor = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'   {self.title}   '