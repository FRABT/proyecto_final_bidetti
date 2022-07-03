from django.db import models


class Comment(models.Model): 
    date = models.DateField()
    blog_title = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return f'   {self.blog_title}   '