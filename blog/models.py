from django.db import models

class Post(models.Model):
    title = models.CharField (max_length=100)
    date = models.DateField (auto_now=True)
    description = models.TextField ()

    def __str__(self):
        desc = str(self.id) + ". " + self.title
        return desc